#!/usr/bin/env python3
"""
Interaktiver KI Book Builder
Ein einfaches Tool zum Erstellen interaktiver Bücher mit Bildern
"""

import json
import os
from typing import List, Dict


class InteractiveBook:
    """Klasse zum Erstellen eines interaktiven Buches"""
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.chapters: List[Dict] = []
    
    def add_chapter(self, chapter_title: str, content: str, image_path: str = None):
        """Fügt ein neues Kapitel zum Buch hinzu"""
        chapter = {
            "title": chapter_title,
            "content": content,
            "image": image_path
        }
        self.chapters.append(chapter)
        print(f"Kapitel '{chapter_title}' wurde hinzugefügt.")
    
    def save_to_json(self, filename: str = "book.json"):
        """Speichert das Buch als JSON-Datei"""
        book_data = {
            "title": self.title,
            "author": self.author,
            "chapters": self.chapters
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(book_data, f, ensure_ascii=False, indent=2)
        
        print(f"Buch wurde als '{filename}' gespeichert.")
    
    def save_to_html(self, filename: str = "book.html"):
        """Speichert das Buch als HTML-Datei"""
        html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <style>
        body {{
            font-family: 'Georgia', serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .book-container {{
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }}
        .author {{
            color: #666;
            font-style: italic;
            margin-bottom: 30px;
        }}
        .chapter {{
            margin-bottom: 40px;
            padding: 20px;
            border-left: 4px solid #4CAF50;
            background-color: #fafafa;
        }}
        .chapter h2 {{
            color: #4CAF50;
            margin-top: 0;
        }}
        .chapter img {{
            max-width: 100%;
            height: auto;
            margin: 20px 0;
            border-radius: 5px;
        }}
        .chapter-content {{
            line-height: 1.6;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="book-container">
        <h1>{self.title}</h1>
        <p class="author">von {self.author}</p>
"""
        
        for i, chapter in enumerate(self.chapters, 1):
            html_content += f"""
        <div class="chapter">
            <h2>Kapitel {i}: {chapter['title']}</h2>
            <div class="chapter-content">
                <p>{chapter['content']}</p>
            </div>
"""
            if chapter.get('image'):
                html_content += f"""            <img src="{chapter['image']}" alt="{chapter['title']}">
"""
            html_content += """        </div>
"""
        
        html_content += """    </div>
</body>
</html>"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Buch wurde als '{filename}' gespeichert.")
    
    def display_info(self):
        """Zeigt Informationen über das Buch an"""
        print(f"\nBuch: {self.title}")
        print(f"Autor: {self.author}")
        print(f"Anzahl Kapitel: {len(self.chapters)}")


def main():
    """Hauptfunktion mit Beispiel-Nutzung"""
    print("=== Interaktiver KI Book Builder ===\n")
    
    # Beispiel: Ein neues Buch erstellen
    book = InteractiveBook(
        title="Mein erstes interaktives Buch",
        author="Book Builder Nutzer"
    )
    
    # Kapitel hinzufügen
    book.add_chapter(
        chapter_title="Einführung",
        content="Dies ist das erste Kapitel meines interaktiven Buches. "
                "Hier kann ich meine Geschichte erzählen und Bilder einfügen.",
        image_path="images/intro.jpg"
    )
    
    book.add_chapter(
        chapter_title="Das Abenteuer beginnt",
        content="In diesem Kapitel beginnt das eigentliche Abenteuer. "
                "Die Möglichkeiten sind endlos!",
        image_path="images/adventure.jpg"
    )
    
    # Informationen anzeigen
    book.display_info()
    
    # Buch speichern
    book.save_to_json("mein_buch.json")
    book.save_to_html("mein_buch.html")
    
    print("\n✓ Buch erfolgreich erstellt!")


if __name__ == "__main__":
    main()
