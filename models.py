"""
Datenmodelle für den Interactive KI Book Builder
"""
from typing import List, Dict, Optional
import json


class Choice:
    """Repräsentiert eine Entscheidungsoption in der Geschichte"""
    
    def __init__(self, text: str, next_section_id: str, label: str = ""):
        self.text = text
        self.next_section_id = next_section_id
        self.label = label  # A, B, C, D
    
    def to_dict(self) -> Dict:
        return {
            "text": self.text,
            "next_section_id": self.next_section_id,
            "label": self.label
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Choice':
        return cls(
            text=data["text"],
            next_section_id=data["next_section_id"],
            label=data.get("label", "")
        )


class Section:
    """Repräsentiert einen Abschnitt in der Geschichte"""
    
    def __init__(self, section_id: str, title: str, content: str, 
                 choices: Optional[List[Choice]] = None,
                 image_prompt: str = "",
                 hints: Optional[List[str]] = None,
                 story_memory: Optional[Dict] = None):
        self.section_id = section_id
        self.title = title
        self.content = content
        self.choices = choices or []
        self.image_prompt = image_prompt
        self.hints = hints or []
        self.story_memory = story_memory or {}
    
    def add_choice(self, choice: Choice):
        self.choices.append(choice)
    
    def is_ending(self) -> bool:
        return len(self.choices) == 0
    
    def to_dict(self) -> Dict:
        return {
            "section_id": self.section_id,
            "title": self.title,
            "content": self.content,
            "choices": [choice.to_dict() for choice in self.choices],
            "image_prompt": self.image_prompt,
            "hints": self.hints,
            "story_memory": self.story_memory
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Section':
        section = cls(
            section_id=data["section_id"],
            title=data["title"],
            content=data["content"],
            image_prompt=data.get("image_prompt", ""),
            hints=data.get("hints", []),
            story_memory=data.get("story_memory", {})
        )
        section.choices = [Choice.from_dict(c) for c in data.get("choices", [])]
        return section


class Story:
    """Repräsentiert eine komplette interaktive Geschichte"""
    
    def __init__(self, title: str, description: str = "", author: str = ""):
        self.title = title
        self.description = description
        self.author = author
        self.sections: Dict[str, Section] = {}
        self.start_section_id = ""
        self.metadata: Dict = {}
    
    def add_section(self, section: Section):
        self.sections[section.section_id] = section
        if not self.start_section_id:
            self.start_section_id = section.section_id
    
    def get_section(self, section_id: str) -> Optional[Section]:
        return self.sections.get(section_id)
    
    def set_start_section(self, section_id: str):
        if section_id in self.sections:
            self.start_section_id = section_id
    
    def get_all_open_paths(self) -> List[str]:
        """Findet alle offenen Pfade (Sections ohne Choices aber nicht als Ende markiert)"""
        open_paths = []
        for section_id, section in self.sections.items():
            if len(section.choices) == 0:
                open_paths.append(section_id)
        return open_paths
    
    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "description": self.description,
            "author": self.author,
            "start_section_id": self.start_section_id,
            "sections": {sid: section.to_dict() for sid, section in self.sections.items()},
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Story':
        story = cls(
            title=data["title"],
            description=data.get("description", ""),
            author=data.get("author", "")
        )
        story.start_section_id = data.get("start_section_id", "")
        story.metadata = data.get("metadata", {})
        
        for section_data in data.get("sections", {}).values():
            section = Section.from_dict(section_data)
            story.add_section(section)
        
        return story
    
    def save_to_file(self, filename: str):
        """Speichert die Story in einer JSON-Datei"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Story':
        """Lädt eine Story aus einer JSON-Datei"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)
