#!/usr/bin/env python3
"""
Hilfsskript zum Erstellen eines neuen interaktiven Buches.
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from book_builder.models import Book, Section, Decision
from book_builder.io import BookIO


def create_template_book():
    """Erstellt ein Template-Buch mit Beispielstruktur."""
    
    print("=" * 80)
    print("  Neues Interaktives Buch Erstellen")
    print("=" * 80)
    print()
    
    # Basisinformationen sammeln
    title = input("Titel des Buches: ").strip()
    if not title:
        title = "Mein Interaktives Abenteuer"
    
    author = input("Autor (Dein Name): ").strip()
    if not author:
        author = "Unbekannt"
    
    description = input("Kurze Beschreibung: ").strip()
    if not description:
        description = "Ein spannendes interaktives Abenteuer"
    
    print()
    print("Erstelle Buch-Template...")
    
    # Buch erstellen
    book = Book(
        title=title,
        author=author,
        description=description,
        start_section_id="start"
    )
    
    # Start-Abschnitt
    start = Section(
        id="start",
        title="Der Beginn",
        text="Deine Geschichte beginnt hier. Beschreibe die Anfangssituation und stelle dem Leser die erste Wahl.",
        decisions=[
            Decision(
                option="A",
                text="Die erste Option wählen",
                next_section_id="weg_a"
            ),
            Decision(
                option="B",
                text="Die zweite Option wählen",
                next_section_id="weg_b"
            )
        ],
        is_ending=False,
        image_prompt=None
    )
    
    # Weg A
    weg_a = Section(
        id="weg_a",
        title="Pfad A",
        text="Du hast Option A gewählt. Was passiert jetzt? Beschreibe die Situation und die Folgen dieser Entscheidung.",
        decisions=[
            Decision(
                option="A",
                text="Weitermachen",
                next_section_id="ende_gut"
            ),
            Decision(
                option="B",
                text="Umkehren",
                next_section_id="ende_neutral"
            )
        ],
        is_ending=False,
        image_prompt=None
    )
    
    # Weg B
    weg_b = Section(
        id="weg_b",
        title="Pfad B",
        text="Du hast Option B gewählt. Was passiert auf diesem Pfad? Beschreibe die einzigartigen Ereignisse dieses Weges.",
        decisions=[
            Decision(
                option="A",
                text="Mutig sein",
                next_section_id="ende_gut"
            ),
            Decision(
                option="B",
                text="Vorsichtig sein",
                next_section_id="ende_schlecht"
            )
        ],
        is_ending=False,
        image_prompt=None
    )
    
    # Ende: Gut
    ende_gut = Section(
        id="ende_gut",
        title="Glückliches Ende",
        text="Herzlichen Glückwunsch! Du hast die beste Entscheidung getroffen. Beschreibe das gute Ende deiner Geschichte.",
        decisions=[],
        is_ending=True,
        image_prompt=None
    )
    
    # Ende: Neutral
    ende_neutral = Section(
        id="ende_neutral",
        title="Neutrales Ende",
        text="Du hast überlebt, aber nicht alles erreicht. Beschreibe dieses gemischte Ende.",
        decisions=[],
        is_ending=True,
        image_prompt=None
    )
    
    # Ende: Schlecht
    ende_schlecht = Section(
        id="ende_schlecht",
        title="Trauriges Ende",
        text="Leider ist deine Geschichte hier zu Ende gegangen. Beschreibe, was schief gelaufen ist.",
        decisions=[],
        is_ending=True,
        image_prompt=None
    )
    
    # Alle Abschnitte zum Buch hinzufügen
    book.add_section(start)
    book.add_section(weg_a)
    book.add_section(weg_b)
    book.add_section(ende_gut)
    book.add_section(ende_neutral)
    book.add_section(ende_schlecht)
    
    # Dateiname erstellen
    safe_filename = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_filename = safe_filename.replace(' ', '_').lower()
    filename = f"{safe_filename}.json"
    
    print()
    filepath = input(f"Dateiname [{filename}]: ").strip()
    if not filepath:
        filepath = filename
    
    # Speichern
    try:
        BookIO.save_book(book, filepath)
        print()
        print("=" * 80)
        print(f"✅ Buch-Template erstellt: {filepath}")
        print("=" * 80)
        print()
        print("Nächste Schritte:")
        print(f"1. Öffne {filepath} in einem Texteditor")
        print("2. Ersetze die Platzhaltertexte mit deiner eigenen Geschichte")
        print("3. Füge weitere Abschnitte und Entscheidungen hinzu")
        print("4. Generiere Bild-Prompts mit:")
        print(f"   python main.py {filepath} --generate-prompts")
        print("5. Spiele deine Geschichte:")
        print(f"   python main.py {filepath}")
        print()
        
        return 0
    except Exception as e:
        print(f"\n❌ Fehler beim Speichern: {e}")
        return 1


def main():
    """Hauptfunktion."""
    try:
        return create_template_book()
    except KeyboardInterrupt:
        print("\n\nAbgebrochen.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
