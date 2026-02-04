"""
KI-Bild-Prompt-Generator für Szenen
"""
from typing import List
import re


class ImagePromptGenerator:
    """Generiert automatisch Bild-Prompts basierend auf Szenen-Beschreibungen"""
    
    def __init__(self):
        self.style_presets = {
            "kinderbuch": "children's book illustration style, colorful, friendly, whimsical",
            "fantasy": "fantasy art, detailed, magical, atmospheric",
            "realistisch": "photorealistic, detailed, cinematic lighting",
            "comic": "comic book style, vibrant colors, dynamic"
        }
        self.default_style = "kinderbuch"
    
    def generate_prompt(self, section_content: str, style: str = None) -> str:
        """
        Generiert einen Bild-Prompt basierend auf dem Abschnittsinhalt
        
        Args:
            section_content: Der Text des Abschnitts
            style: Gewünschter Stil (kinderbuch, fantasy, realistisch, comic)
        
        Returns:
            Ein formatierter Bild-Prompt
        """
        if style is None:
            style = self.default_style
        
        # Extrahiere Schlüsselelemente aus dem Text
        keywords = self._extract_keywords(section_content)
        
        # Basis-Prompt mit Schlüsselwörtern
        prompt_parts = []
        
        # Füge Stil-Preset hinzu
        if style in self.style_presets:
            prompt_parts.append(self.style_presets[style])
        
        # Füge extrahierte Keywords hinzu
        if keywords:
            prompt_parts.append(", ".join(keywords[:5]))  # Maximal 5 Keywords
        
        # Erstelle finalen Prompt
        final_prompt = ", ".join(prompt_parts)
        
        return final_prompt
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extrahiert wichtige Schlüsselwörter aus dem Text"""
        # Einfache Keyword-Extraktion basierend auf häufigen Substantiven
        # In einer echten Implementierung würde man hier NLP verwenden
        
        # Entferne Satzzeichen
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        
        # Deutsche Stop-Wörter (vereinfacht)
        stop_words = {
            'der', 'die', 'das', 'und', 'oder', 'aber', 'ist', 'sind', 
            'war', 'waren', 'ein', 'eine', 'einen', 'du', 'sie', 'er',
            'es', 'wir', 'ihr', 'in', 'auf', 'an', 'zu', 'mit', 'von',
            'für', 'nicht', 'sich', 'bei', 'nach', 'vor', 'durch'
        }
        
        # Interessante Wörter (Substantive, Adjektive)
        words = text.split()
        keywords = []
        
        for word in words:
            if len(word) > 3 and word not in stop_words:
                keywords.append(word)
        
        # Entferne Duplikate und behalte Reihenfolge
        seen = set()
        unique_keywords = []
        for kw in keywords:
            if kw not in seen:
                seen.add(kw)
                unique_keywords.append(kw)
        
        return unique_keywords[:10]  # Maximal 10 Keywords
    
    def generate_auto_prompt_for_section(self, section_title: str, section_content: str, style: str = None) -> str:
        """
        Generiert einen aussagekräftigen Prompt basierend auf Titel und Inhalt
        
        Args:
            section_title: Titel des Abschnitts
            section_content: Inhalt des Abschnitts
            style: Gewünschter Visueller Stil
        
        Returns:
            Vollständiger Bild-Prompt
        """
        # Kombiniere Titel und Inhalt
        combined_text = f"{section_title}. {section_content}"
        
        return self.generate_prompt(combined_text, style)
