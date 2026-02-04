"""
Generator für KI-Bildprompts basierend auf Szenen.
"""

from typing import Optional
from .models import Section


class ImagePromptGenerator:
    """Generiert Bild-Prompts für Szenen."""
    
    @staticmethod
    def generate_prompt(section: Section, style: str = "fantasy art") -> str:
        """
        Generiert einen KI-Bildprompt für einen Abschnitt.
        
        Args:
            section: Der Abschnitt, für den ein Prompt generiert werden soll
            style: Der gewünschte Kunststil (Standard: "fantasy art")
            
        Returns:
            Ein kopierfreundlicher Bildprompt
        """
        # Extrahiere Schlüsselwörter aus dem Titel und Text
        title_keywords = section.title.lower()
        
        # Basis-Prompt erstellen
        prompt_parts = [
            f"Scene: {section.title}",
            f"Style: {style}, detailed illustration, high quality",
        ]
        
        # Textausschnitt für Kontext (erste 200 Zeichen)
        text_snippet = section.text[:200].replace('\n', ' ').strip()
        if len(section.text) > 200:
            text_snippet += "..."
        
        prompt_parts.append(f"Description: {text_snippet}")
        
        # Atmosphäre basierend auf Schlüsselwörtern
        atmosphere_keywords = {
            'dunkel': 'dark atmosphere, mysterious',
            'hell': 'bright atmosphere, cheerful',
            'wald': 'forest setting, natural light',
            'stadt': 'urban setting, cityscape',
            'gefahr': 'dangerous atmosphere, tense',
            'frieden': 'peaceful atmosphere, calm',
            'magie': 'magical atmosphere, mystical',
            'kampf': 'battle scene, dynamic action',
            'schloss': 'castle setting, medieval',
            'höhle': 'cave setting, underground'
        }
        
        detected_atmosphere = []
        text_lower = (section.title + " " + section.text).lower()
        for keyword, atmosphere in atmosphere_keywords.items():
            if keyword in text_lower:
                detected_atmosphere.append(atmosphere)
        
        if detected_atmosphere:
            prompt_parts.append(f"Atmosphere: {', '.join(detected_atmosphere[:3])}")
        
        # Zusammenfügen
        full_prompt = " | ".join(prompt_parts)
        
        return full_prompt
    
    @staticmethod
    def generate_prompt_for_all_sections(book) -> None:
        """
        Generiert Bild-Prompts für alle Abschnitte eines Buches.
        
        Args:
            book: Das Buch, für das Prompts generiert werden sollen
        """
        for section_id, section in book.sections.items():
            if not section.image_prompt:
                section.image_prompt = ImagePromptGenerator.generate_prompt(section)
