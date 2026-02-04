#!/usr/bin/env python3
"""
Interaktiver Book Builder - Haupteinstiegspunkt
Ermöglicht das Erstellen und Ausführen von interaktiven Gamebooks mit Bildern.
"""

import argparse
import json
import sys
from pathlib import Path


def load_gamebook(filepath):
    """Lade ein Gamebook aus einer JSON-Datei."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Fehler: Datei '{filepath}' nicht gefunden.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: Ungültiges JSON in '{filepath}': {e}")
        sys.exit(1)


def display_scene(scene):
    """Zeige eine Szene aus dem Gamebook an."""
    print("\n" + "=" * 60)
    print(f"\n{scene.get('title', 'Unbenannte Szene')}")
    print("-" * 60)
    print(f"\n{scene.get('text', '')}\n")
    
    if 'image' in scene:
        print(f"[Bild: {scene['image']}]")
    
    choices = scene.get('choices', [])
    if choices:
        print("\nAuswahlmöglichkeiten:")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice.get('text', 'Weiter')}")
    else:
        print("\n[Ende der Geschichte]")
    
    print("=" * 60)


def run_gamebook(gamebook_data):
    """Führe ein interaktives Gamebook aus."""
    print("\n" + "=" * 60)
    print(f"  {gamebook_data.get('title', 'Interaktives Gamebook')}")
    print("=" * 60)
    
    if 'description' in gamebook_data:
        print(f"\n{gamebook_data['description']}\n")
    
    scenes = gamebook_data.get('scenes', [])
    if not scenes:
        print("Fehler: Keine Szenen im Gamebook gefunden.")
        return
    
    current_scene_id = gamebook_data.get('start_scene', scenes[0].get('id', 0))
    
    while True:
        # Finde aktuelle Szene
        current_scene = None
        for scene in scenes:
            if scene.get('id') == current_scene_id:
                current_scene = scene
                break
        
        if not current_scene:
            print(f"\nFehler: Szene '{current_scene_id}' nicht gefunden.")
            break
        
        # Zeige die Szene an
        display_scene(current_scene)
        
        # Hole Auswahlmöglichkeiten
        choices = current_scene.get('choices', [])
        if not choices:
            # Ende der Geschichte
            break
        
        # Hole Benutzereingabe
        while True:
            try:
                choice_input = input("\nGib deine Wahl ein (Zahl oder 'q' zum Beenden): ").strip()
                
                if choice_input.lower() == 'q':
                    print("\nDanke fürs Spielen!")
                    return
                
                choice_num = int(choice_input)
                if 1 <= choice_num <= len(choices):
                    selected_choice = choices[choice_num - 1]
                    current_scene_id = selected_choice.get('next_scene')
                    if current_scene_id is None:
                        print("\nEnde der Geschichte. Danke fürs Spielen!")
                        return
                    break
                else:
                    print(f"Bitte gib eine Zahl zwischen 1 und {len(choices)} ein.")
            except ValueError:
                print("Bitte gib eine gültige Zahl oder 'q' zum Beenden ein.")
            except (KeyboardInterrupt, EOFError):
                print("\n\nDanke fürs Spielen!")
                return


def main():
    """Haupteinstiegspunkt für die Anwendung."""
    parser = argparse.ArgumentParser(
        description='Interaktiver Book Builder - Erstelle und spiele interaktive Gamebooks'
    )
    parser.add_argument(
        '--example',
        type=str,
        help='Pfad zu einer Beispiel-Gamebook-JSON-Datei zum Laden und Spielen'
    )
    
    args = parser.parse_args()
    
    if args.example:
        # Lade und führe das Beispiel-Gamebook aus
        example_path = Path(args.example)
        print(f"Lade Beispiel von: {example_path}")
        gamebook_data = load_gamebook(example_path)
        run_gamebook(gamebook_data)
    else:
        # Keine Argumente angegeben, zeige Hilfe
        parser.print_help()
        print("\nBeispielverwendung:")
        print("  python src/main.py --example examples/mini_gamebook.json")


if __name__ == '__main__':
    main()
