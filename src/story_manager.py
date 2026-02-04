"""
Story Manager - Verwaltet Geschichten und erstellt interaktive Bücher
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


class StoryManager:
    """Verwaltet das Laden und Verarbeiten von Geschichten"""
    
    def __init__(self, input_file: str):
        """
        Initialisiert den Story Manager
        
        Args:
            input_file: Pfad zur JSON-Datei mit der Geschichte
        """
        self.input_file = Path(input_file)
        self.story_data = None
    
    def load_story(self) -> Dict[str, Any]:
        """
        Lädt die Geschichte aus der JSON-Datei
        
        Returns:
            Dictionary mit den Geschichtsdaten
        
        Raises:
            FileNotFoundError: Wenn die Datei nicht existiert
            json.JSONDecodeError: Wenn die JSON-Datei ungültig ist
        """
        if not self.input_file.exists():
            raise FileNotFoundError(f"Datei nicht gefunden: {self.input_file}")
        
        with open(self.input_file, 'r', encoding='utf-8') as f:
            self.story_data = json.load(f)
        
        # Validierung der Struktur
        self._validate_story_structure(self.story_data)
        
        return self.story_data
    
    def _validate_story_structure(self, data: Dict[str, Any]) -> None:
        """
        Validiert die Struktur der Geschichtsdaten
        
        Args:
            data: Dictionary mit den Geschichtsdaten
        
        Raises:
            ValueError: Wenn die Struktur ungültig ist
        """
        required_fields = ['title', 'pages']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Pflichtfeld fehlt: {field}")
        
        if not isinstance(data['pages'], list):
            raise ValueError("'pages' muss eine Liste sein")
        
        if len(data['pages']) == 0:
            raise ValueError("Geschichte muss mindestens eine Seite haben")
    
    def get_pages(self) -> List[Dict[str, Any]]:
        """
        Gibt alle Seiten der Geschichte zurück
        
        Returns:
            Liste von Seiten-Dictionaries
        """
        if not self.story_data:
            raise ValueError("Geschichte wurde noch nicht geladen")
        
        return self.story_data.get('pages', [])
    
    def create_book(
        self,
        story_data: Dict[str, Any],
        output_dir: str,
        include_images: bool = True
    ) -> str:
        """
        Erstellt das interaktive Buch im Ausgabeverzeichnis
        
        Args:
            story_data: Dictionary mit den Geschichtsdaten
            output_dir: Zielverzeichnis für das Buch
            include_images: Ob Bilder eingebunden werden sollen
        
        Returns:
            Pfad zum erstellten Buch
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # HTML-Datei erstellen
        html_file = output_path / 'book.html'
        html_content = self._generate_html(story_data, include_images)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # JSON-Datei speichern
        json_file = output_path / 'story.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(story_data, f, ensure_ascii=False, indent=2)
        
        return str(html_file)
    
    def _generate_html(
        self,
        story_data: Dict[str, Any],
        include_images: bool
    ) -> str:
        """
        Generiert HTML für das interaktive Buch
        
        Args:
            story_data: Dictionary mit den Geschichtsdaten
            include_images: Ob Bilder eingebunden werden sollen
        
        Returns:
            HTML-String
        """
        title = story_data.get('title', 'Mein interaktives Buch')
        pages = story_data.get('pages', [])
        
        html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .page {{ display: none; margin: 20px 0; }}
        .page.active {{ display: block; }}
        .choice {{ margin: 10px 0; padding: 10px; background: #f0f0f0; cursor: pointer; }}
        .choice:hover {{ background: #e0e0e0; }}
        img {{ max-width: 100%; height: auto; }}
        h1 {{ color: #333; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div id="book">
"""
        
        for i, page in enumerate(pages):
            page_id = page.get('id', i)
            text = page.get('text', '')
            choices = page.get('choices', [])
            
            html += f'        <div class="page" id="page-{page_id}">\n'
            html += f'            <p>{text}</p>\n'
            
            if include_images and 'image' in page:
                html += f'            <img src="{page["image"]}" alt="Illustration">\n'
            
            if choices:
                html += '            <div class="choices">\n'
                for choice in choices:
                    choice_text = choice.get('text', '')
                    next_page = choice.get('next', '')
                    html += f'                <div class="choice" onclick="goToPage(\'{next_page}\')">{choice_text}</div>\n'
                html += '            </div>\n'
            
            html += '        </div>\n'
        
        html += """    </div>
    <script>
        function goToPage(pageId) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById('page-' + pageId).classList.add('active');
        }
        // Erste Seite anzeigen
        document.querySelector('.page').classList.add('active');
    </script>
</body>
</html>
"""
        return html
