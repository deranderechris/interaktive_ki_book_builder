#!/usr/bin/env python3
"""
Haupteinstiegspunkt für den Interaktiven KI Book Builder.
"""

import sys
import argparse
from pathlib import Path

# Füge das Parent-Verzeichnis zum Python-Pfad hinzu
sys.path.insert(0, str(Path(__file__).parent))

from book_builder.models import Book
from book_builder.io import BookIO
from book_builder.cli import CLI
from book_builder.image_prompt import ImagePromptGenerator


def main():
    """Hauptfunktion."""
    parser = argparse.ArgumentParser(
        description='Interaktiver KI Book Builder - Erstelle und erlebe interaktive Geschichten'
    )
    parser.add_argument(
        'book_file',
        nargs='?',
        default='examples/beispiel_buch.json',
        help='Pfad zur Buch-JSON-Datei (Standard: examples/beispiel_buch.json)'
    )
    parser.add_argument(
        '--generate-prompts',
        action='store_true',
        help='Generiere Bild-Prompts für alle Abschnitte ohne vorhandene Prompts'
    )
    
    args = parser.parse_args()
    
    # Lade das Buch
    try:
        book_path = Path(args.book_file)
        if not book_path.exists():
            print(f"❌ Fehler: Buch-Datei '{args.book_file}' nicht gefunden!")
            print(f"\nVerwende das Beispielbuch mit:")
            print(f"  python main.py examples/beispiel_buch.json")
            return 1
        
        book = BookIO.load_book(str(book_path))
        print(f"✅ Buch geladen: {book.title}")
        
        # Generiere Prompts wenn gewünscht
        if args.generate_prompts:
            print("\n🎨 Generiere Bild-Prompts...")
            ImagePromptGenerator.generate_prompt_for_all_sections(book)
            BookIO.save_book(book, str(book_path))
            print(f"✅ Bild-Prompts generiert und gespeichert in '{args.book_file}'")
            return 0
        
        # Starte die CLI
        print(f"\n🎮 Starte interaktive Geschichte...\n")
        cli = CLI(book)
        cli.run()
        
        return 0
        
    except FileNotFoundError:
        print(f"❌ Fehler: Datei '{args.book_file}' nicht gefunden!")
        return 1
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
