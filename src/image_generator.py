"""
Image Generator - Generiert Bilder mit KI für die Geschichte
"""

import os
from typing import Dict, List, Any
from pathlib import Path


class ImageGenerator:
    """Generiert Bilder für Geschichtenseiten mit KI"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialisiert den Image Generator
        
        Args:
            config: Konfigurationsdictionary mit API-Einstellungen
        """
        self.config = config
        self.api_key = config.get('openai_api_key', os.getenv('OPENAI_API_KEY'))
        self.model = config.get('image_model', 'dall-e-3')
        
        if not self.api_key:
            raise ValueError(
                "OpenAI API Key fehlt. Bitte in .env oder config.json angeben."
            )
    
    def generate_images(
        self,
        story_data: Dict[str, Any],
        output_dir: str = 'output/images'
    ) -> List[str]:
        """
        Generiert Bilder für alle Seiten der Geschichte
        
        Args:
            story_data: Dictionary mit den Geschichtsdaten
            output_dir: Verzeichnis für die generierten Bilder
        
        Returns:
            Liste der Pfade zu den generierten Bildern
        """
        pages = story_data.get('pages', [])
        image_paths = []
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for i, page in enumerate(pages):
            if 'image_prompt' in page:
                image_path = self._generate_image(
                    page['image_prompt'],
                    output_path / f"page_{i}.png"
                )
                image_paths.append(image_path)
                page['image'] = str(image_path)
        
        return image_paths
    
    def _generate_image(self, prompt: str, output_path: Path) -> str:
        """
        Generiert ein einzelnes Bild basierend auf dem Prompt
        
        Args:
            prompt: Beschreibung des zu generierenden Bildes
            output_path: Pfad für das Ausgabebild
        
        Returns:
            Pfad zum generierten Bild
        """
        # Placeholder-Implementierung
        # In einer echten Implementierung würde hier die OpenAI API aufgerufen
        try:
            # from openai import OpenAI
            # client = OpenAI(api_key=self.api_key)
            # 
            # response = client.images.generate(
            #     model=self.model,
            #     prompt=prompt,
            #     size="1024x1024",
            #     quality="standard",
            #     n=1,
            # )
            # 
            # image_url = response.data[0].url
            # # Bild herunterladen und speichern
            # import requests
            # img_data = requests.get(image_url).content
            # with open(output_path, 'wb') as f:
            #     f.write(img_data)
            
            # Für Demo-Zwecke erstellen wir ein Placeholder-Bild
            self._create_placeholder_image(output_path, prompt)
            
            return str(output_path)
        
        except Exception as e:
            raise RuntimeError(f"Fehler beim Generieren des Bildes: {e}")
    
    def _create_placeholder_image(self, output_path: Path, text: str) -> None:
        """
        Erstellt ein Placeholder-Bild für Demo-Zwecke
        
        Args:
            output_path: Pfad für das Ausgabebild
            text: Text, der auf dem Placeholder angezeigt werden soll
        """
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # Erstelle ein einfaches Bild
            img = Image.new('RGB', (800, 600), color=(200, 200, 200))
            d = ImageDraw.Draw(img)
            
            # Text auf dem Bild
            wrapped_text = self._wrap_text(text, 40)
            d.text((50, 250), wrapped_text, fill=(0, 0, 0))
            
            # Bild speichern
            img.save(output_path)
        
        except ImportError:
            # Falls PIL nicht verfügbar ist, erstelle leere Datei
            output_path.touch()
    
    def _wrap_text(self, text: str, width: int) -> str:
        """
        Bricht Text in mehrere Zeilen um
        
        Args:
            text: Zu umbrechender Text
            width: Maximale Zeilenbreite
        
        Returns:
            Umgebrochener Text
        """
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
