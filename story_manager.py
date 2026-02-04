"""
Story-Manager für die Verwaltung interaktiver Geschichten
"""
from models import Story, Section, Choice
from image_prompt_generator import ImagePromptGenerator
from typing import Optional


class StoryManager:
    """Verwaltet das Erstellen und Bearbeiten von Geschichten"""
    
    def __init__(self):
        self.current_story: Optional[Story] = None
        self.prompt_generator = ImagePromptGenerator()
    
    def create_new_story(self, title: str, description: str = "", author: str = "") -> Story:
        """Erstellt eine neue Story"""
        self.current_story = Story(title=title, description=description, author=author)
        return self.current_story
    
    def load_story(self, filename: str) -> Story:
        """Lädt eine Story aus einer Datei"""
        self.current_story = Story.load_from_file(filename)
        return self.current_story
    
    def save_story(self, filename: str):
        """Speichert die aktuelle Story"""
        if self.current_story:
            self.current_story.save_to_file(filename)
    
    def add_section(self, section_id: str, title: str, content: str, 
                   auto_generate_image_prompt: bool = True) -> Section:
        """Fügt einen neuen Abschnitt zur Story hinzu"""
        if not self.current_story:
            raise ValueError("Keine Story geladen. Erstelle zuerst eine neue Story.")
        
        # Generiere automatisch Image Prompt wenn gewünscht
        image_prompt = ""
        if auto_generate_image_prompt:
            image_prompt = self.prompt_generator.generate_auto_prompt_for_section(
                title, content
            )
        
        section = Section(
            section_id=section_id,
            title=title,
            content=content,
            image_prompt=image_prompt
        )
        
        self.current_story.add_section(section)
        return section
    
    def add_choice_to_section(self, section_id: str, choice_text: str, 
                             next_section_id: str, label: str = "") -> bool:
        """Fügt eine Entscheidung zu einem Abschnitt hinzu"""
        if not self.current_story:
            return False
        
        section = self.current_story.get_section(section_id)
        if not section:
            return False
        
        choice = Choice(text=choice_text, next_section_id=next_section_id, label=label)
        section.add_choice(choice)
        return True
    
    def add_hint_to_section(self, section_id: str, hint: str) -> bool:
        """Fügt einen Hinweis zu einem Abschnitt hinzu"""
        if not self.current_story:
            return False
        
        section = self.current_story.get_section(section_id)
        if not section:
            return False
        
        section.hints.append(hint)
        return True
    
    def set_story_memory(self, section_id: str, key: str, value: str) -> bool:
        """Setzt einen Story-Gedächtnis-Eintrag für einen Abschnitt"""
        if not self.current_story:
            return False
        
        section = self.current_story.get_section(section_id)
        if not section:
            return False
        
        section.story_memory[key] = value
        return True
    
    def get_story_info(self) -> dict:
        """Gibt Informationen über die aktuelle Story zurück"""
        if not self.current_story:
            return {"error": "Keine Story geladen"}
        
        return {
            "title": self.current_story.title,
            "description": self.current_story.description,
            "author": self.current_story.author,
            "section_count": len(self.current_story.sections),
            "start_section": self.current_story.start_section_id,
            "open_paths": self.current_story.get_all_open_paths()
        }
    
    def list_sections(self) -> list:
        """Listet alle Abschnitte der aktuellen Story auf"""
        if not self.current_story:
            return []
        
        sections_info = []
        for section_id, section in self.current_story.sections.items():
            sections_info.append({
                "id": section_id,
                "title": section.title,
                "choices_count": len(section.choices),
                "is_ending": section.is_ending()
            })
        
        return sections_info
