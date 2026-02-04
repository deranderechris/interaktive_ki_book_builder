"""
JSON Import/Export Funktionalität für interaktive Bücher.
"""

import json
from pathlib import Path
from typing import Dict
from .models import Book, Memory


class BookIO:
    """Klasse für Import und Export von Büchern."""
    
    @staticmethod
    def save_book(book: Book, filepath: str) -> None:
        """
        Speichert ein Buch als JSON-Datei.
        
        Args:
            book: Das zu speichernde Buch
            filepath: Pfad zur JSON-Datei
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(book.to_dict(), f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def load_book(filepath: str) -> Book:
        """
        Lädt ein Buch aus einer JSON-Datei.
        
        Args:
            filepath: Pfad zur JSON-Datei
            
        Returns:
            Das geladene Buch
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Book.from_dict(data)
    
    @staticmethod
    def save_memory(memory: Memory, filepath: str) -> None:
        """
        Speichert den Gedächtniszustand als JSON-Datei.
        
        Args:
            memory: Das zu speichernde Gedächtnis
            filepath: Pfad zur JSON-Datei
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(memory.to_dict(), f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def load_memory(filepath: str) -> Memory:
        """
        Lädt den Gedächtniszustand aus einer JSON-Datei.
        
        Args:
            filepath: Pfad zur JSON-Datei
            
        Returns:
            Das geladene Gedächtnis
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Memory.from_dict(data)
