"""
CLI-Menüsystem für die Navigation durch interaktive Geschichten.
"""

import os
import sys
from typing import Optional
from .models import Book, Memory, Section
from .io import BookIO
from .image_prompt import ImagePromptGenerator


class CLI:
    """Command Line Interface für das interaktive Buchsystem."""
    
    def __init__(self, book: Book):
        """
        Initialisiert die CLI mit einem Buch.
        
        Args:
            book: Das interaktive Buch
        """
        self.book = book
        self.memory = Memory()
        self.current_section_id = book.start_section_id
        self.running = True
    
    def clear_screen(self):
        """Löscht den Bildschirm."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Zeigt den Header an."""
        print("=" * 80)
        print(f"  {self.book.title}")
        print(f"  von {self.book.author}")
        print("=" * 80)
        print()
    
    def print_section(self, section: Section):
        """
        Zeigt einen Abschnitt an.
        
        Args:
            section: Der anzuzeigende Abschnitt
        """
        print(f"\n### {section.title} ###\n")
        print(section.text)
        print()
        
        # Bild-Prompt anzeigen wenn vorhanden
        if section.image_prompt:
            print("📸 BILD-PROMPT (kopierbar):")
            print("-" * 80)
            print(section.image_prompt)
            print("-" * 80)
            print()
    
    def show_decisions(self, section: Section):
        """
        Zeigt verfügbare Entscheidungen an.
        
        Args:
            section: Der Abschnitt mit Entscheidungen
        """
        if section.is_ending:
            print("\n🏁 ENDE dieser Geschichte!\n")
            return
        
        print("\nWas möchtest du tun?\n")
        for decision in section.decisions:
            print(f"  [{decision.option}] {decision.text}")
        print()
    
    def show_memory(self):
        """Zeigt den Gedächtniszustand an."""
        print("\n=== GEDÄCHTNIS ===")
        print(f"\nBesuchte Abschnitte: {len(self.memory.visited_sections)}")
        print(f"Getroffene Entscheidungen: {len(self.memory.decisions_made)}")
        
        if self.memory.hints:
            print(f"\n📝 Hinweise ({len(self.memory.hints)}):")
            for i, hint in enumerate(self.memory.hints, 1):
                print(f"  {i}. {hint}")
        
        if self.memory.open_paths:
            print(f"\n🔓 Offene Pfade ({len(self.memory.open_paths)}):")
            for i, path in enumerate(self.memory.open_paths, 1):
                print(f"  {i}. {path}")
        
        if self.memory.summary:
            print(f"\n📖 Zusammenfassung:")
            print(f"  {self.memory.summary}")
        
        print("\n" + "=" * 80)
        input("\nDrücke Enter, um fortzufahren...")
    
    def show_decision_history(self):
        """Zeigt die Historie der getroffenen Entscheidungen."""
        if not self.memory.decisions_made:
            print("\nNoch keine Entscheidungen getroffen.")
            return
        
        print("\n=== ENTSCHEIDUNGSHISTORIE ===\n")
        for decision in self.memory.decisions_made:
            section = self.book.get_section(decision['section_id'])
            section_title = section.title if section else "Unbekannt"
            print(f"{decision['order']}. {section_title}: Option {decision['decision']}")
        
        print("\n" + "=" * 80)
        input("\nDrücke Enter, um fortzufahren...")
    
    def main_menu(self):
        """Zeigt das Hauptmenü an."""
        while self.running:
            self.clear_screen()
            self.print_header()
            
            print("HAUPTMENÜ\n")
            print("  [1] Neue Geschichte starten")
            print("  [2] Geschichte fortsetzen")
            print("  [3] Gedächtnis anzeigen")
            print("  [4] Entscheidungshistorie anzeigen")
            print("  [5] Fortschritt speichern")
            print("  [6] Fortschritt laden")
            print("  [7] Beenden")
            print()
            
            choice = input("Wähle eine Option: ").strip()
            
            if choice == "1":
                self.start_new_story()
            elif choice == "2":
                self.continue_story()
            elif choice == "3":
                self.show_memory()
            elif choice == "4":
                self.show_decision_history()
            elif choice == "5":
                self.save_progress()
            elif choice == "6":
                self.load_progress()
            elif choice == "7":
                print("\nAuf Wiedersehen!")
                self.running = False
            else:
                print("\nUngültige Auswahl!")
                input("Drücke Enter, um fortzufahren...")
    
    def start_new_story(self):
        """Startet eine neue Geschichte."""
        self.memory = Memory()
        self.current_section_id = self.book.start_section_id
        print("\n✨ Neue Geschichte gestartet!\n")
        input("Drücke Enter, um fortzufahren...")
        self.continue_story()
    
    def continue_story(self):
        """Setzt die Geschichte fort."""
        while True:
            section = self.book.get_section(self.current_section_id)
            
            if not section:
                print(f"\n❌ Fehler: Abschnitt '{self.current_section_id}' nicht gefunden!")
                input("Drücke Enter, um zum Hauptmenü zurückzukehren...")
                break
            
            # Abschnitt zum Gedächtnis hinzufügen
            self.memory.add_visit(section.id)
            
            # Abschnitt anzeigen
            self.clear_screen()
            self.print_header()
            self.print_section(section)
            
            # Wenn es ein Ende ist
            if section.is_ending:
                self.show_decisions(section)
                input("\nDrücke Enter, um zum Hauptmenü zurückzukehren...")
                break
            
            # Entscheidungen anzeigen
            self.show_decisions(section)
            
            # Zusätzliche Optionen
            print("  [M] Zurück zum Hauptmenü")
            print("  [G] Gedächtnis anzeigen")
            print()
            
            choice = input("Deine Wahl: ").strip().upper()
            
            if choice == "M":
                break
            elif choice == "G":
                self.show_memory()
                continue
            
            # Prüfe ob die Wahl gültig ist
            valid_options = [d.option for d in section.decisions]
            if choice not in valid_options:
                print("\n❌ Ungültige Wahl!")
                input("Drücke Enter, um fortzufahren...")
                continue
            
            # Finde die gewählte Entscheidung
            chosen_decision = next(d for d in section.decisions if d.option == choice)
            
            # Speichere die Entscheidung
            self.memory.add_decision(section.id, choice)
            
            # Gehe zum nächsten Abschnitt
            self.current_section_id = chosen_decision.next_section_id
    
    def save_progress(self):
        """Speichert den aktuellen Fortschritt."""
        filepath = input("\nDateiname für Speicherstand (z.B. save.json): ").strip()
        if not filepath:
            filepath = "save.json"
        
        try:
            # Erstelle einen erweiterten Speicherstand
            save_data = self.memory.to_dict()
            save_data['current_section_id'] = self.current_section_id
            
            import json
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Fortschritt gespeichert in '{filepath}'")
        except Exception as e:
            print(f"\n❌ Fehler beim Speichern: {e}")
        
        input("Drücke Enter, um fortzufahren...")
    
    def load_progress(self):
        """Lädt einen gespeicherten Fortschritt."""
        filepath = input("\nDateiname des Speicherstands (z.B. save.json): ").strip()
        if not filepath:
            filepath = "save.json"
        
        try:
            import json
            with open(filepath, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            self.memory = Memory.from_dict(save_data)
            self.current_section_id = save_data.get('current_section_id', self.book.start_section_id)
            
            print(f"\n✅ Fortschritt geladen aus '{filepath}'")
        except FileNotFoundError:
            print(f"\n❌ Datei '{filepath}' nicht gefunden!")
        except Exception as e:
            print(f"\n❌ Fehler beim Laden: {e}")
        
        input("Drücke Enter, um fortzufahren...")
    
    def run(self):
        """Startet die CLI."""
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen!")
            sys.exit(0)
