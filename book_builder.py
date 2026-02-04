#!/usr/bin/env python3
"""
Interactive KI Book Builder - Hauptanwendung
Ein interaktiver KI-Book-Builder für personalisierte Geschichten
"""
import sys
import os
from story_manager import StoryManager
from exporter import StoryExporter


class BookBuilder:
    """Hauptanwendung für den Interactive KI Book Builder"""
    
    def __init__(self):
        self.manager = StoryManager()
        self.running = True
    
    def display_menu(self):
        """Zeigt das Hauptmenü an"""
        print("\n" + "="*60)
        print("  INTERACTIVE KI BOOK BUILDER")
        print("="*60)
        
        if self.manager.current_story:
            info = self.manager.get_story_info()
            print(f"\nAktuelle Story: {info['title']}")
            print(f"Abschnitte: {info['section_count']}")
        else:
            print("\nKeine Story geladen")
        
        print("\n--- Hauptmenü ---")
        print("1. Neue Story erstellen")
        print("2. Story laden")
        print("3. Story speichern")
        print("4. Abschnitt hinzufügen")
        print("5. Entscheidung hinzufügen")
        print("6. Story-Informationen anzeigen")
        print("7. Alle Abschnitte auflisten")
        print("8. Story exportieren")
        print("9. Beispiel 'Zauberwald' laden")
        print("0. Beenden")
        print()
    
    def create_new_story(self):
        """Erstellt eine neue Story"""
        print("\n--- Neue Story erstellen ---")
        title = input("Titel der Story: ").strip()
        if not title:
            print("Fehler: Titel darf nicht leer sein")
            return
        
        description = input("Beschreibung (optional): ").strip()
        author = input("Autor (optional): ").strip()
        
        self.manager.create_new_story(title, description, author)
        print(f"\n✓ Story '{title}' wurde erstellt!")
    
    def load_story(self):
        """Lädt eine Story aus einer Datei"""
        print("\n--- Story laden ---")
        filename = input("Dateiname (z.B. story.json): ").strip()
        
        if not os.path.exists(filename):
            print(f"Fehler: Datei '{filename}' nicht gefunden")
            return
        
        try:
            self.manager.load_story(filename)
            print(f"\n✓ Story wurde geladen!")
        except Exception as e:
            print(f"Fehler beim Laden: {e}")
    
    def save_story(self):
        """Speichert die aktuelle Story"""
        if not self.manager.current_story:
            print("\nFehler: Keine Story geladen")
            return
        
        print("\n--- Story speichern ---")
        filename = input("Dateiname (z.B. story.json): ").strip()
        
        if not filename.endswith('.json'):
            filename += '.json'
        
        try:
            self.manager.save_story(filename)
            print(f"\n✓ Story wurde gespeichert: {filename}")
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
    
    def add_section(self):
        """Fügt einen neuen Abschnitt hinzu"""
        if not self.manager.current_story:
            print("\nFehler: Keine Story geladen")
            return
        
        print("\n--- Neuen Abschnitt hinzufügen ---")
        section_id = input("Abschnitt-ID (z.B. S1, S2, ...): ").strip()
        
        if self.manager.current_story.get_section(section_id):
            print(f"Fehler: Abschnitt '{section_id}' existiert bereits")
            return
        
        title = input("Titel des Abschnitts: ").strip()
        print("Inhalt des Abschnitts (mehrere Zeilen möglich, leere Zeile zum Beenden):")
        
        content_lines = []
        while True:
            line = input()
            if line == "":
                break
            content_lines.append(line)
        
        content = "\n".join(content_lines)
        
        auto_prompt = input("Automatisch Bild-Prompt generieren? (j/n): ").strip().lower()
        auto_generate = auto_prompt == 'j'
        
        section = self.manager.add_section(section_id, title, content, auto_generate)
        
        print(f"\n✓ Abschnitt '{section_id}' wurde hinzugefügt!")
        if section.image_prompt:
            print(f"📸 Generierter Bild-Prompt: {section.image_prompt}")
        
        # Frage ob Start-Section gesetzt werden soll
        if len(self.manager.current_story.sections) == 1:
            self.manager.current_story.set_start_section(section_id)
            print(f"✓ '{section_id}' wurde als Start-Abschnitt gesetzt")
    
    def add_choice(self):
        """Fügt eine Entscheidung zu einem Abschnitt hinzu"""
        if not self.manager.current_story:
            print("\nFehler: Keine Story geladen")
            return
        
        print("\n--- Entscheidung hinzufügen ---")
        section_id = input("Abschnitt-ID: ").strip()
        
        if not self.manager.current_story.get_section(section_id):
            print(f"Fehler: Abschnitt '{section_id}' nicht gefunden")
            return
        
        choice_text = input("Text der Entscheidung: ").strip()
        next_section = input("Ziel-Abschnitt-ID: ").strip()
        label = input("Label (A/B/C/D, optional): ").strip().upper()
        
        success = self.manager.add_choice_to_section(section_id, choice_text, next_section, label)
        
        if success:
            print(f"\n✓ Entscheidung wurde zu Abschnitt '{section_id}' hinzugefügt!")
        else:
            print("\nFehler beim Hinzufügen der Entscheidung")
    
    def show_story_info(self):
        """Zeigt Informationen über die Story an"""
        if not self.manager.current_story:
            print("\nKeine Story geladen")
            return
        
        info = self.manager.get_story_info()
        
        print("\n" + "="*60)
        print("  STORY-INFORMATIONEN")
        print("="*60)
        print(f"\nTitel: {info['title']}")
        print(f"Beschreibung: {info['description']}")
        print(f"Autor: {info['author']}")
        print(f"Anzahl Abschnitte: {info['section_count']}")
        print(f"Start-Abschnitt: {info['start_section']}")
        
        if info['open_paths']:
            print(f"\nOffene Pfade (Enden): {', '.join(info['open_paths'])}")
    
    def list_sections(self):
        """Listet alle Abschnitte auf"""
        if not self.manager.current_story:
            print("\nKeine Story geladen")
            return
        
        sections = self.manager.list_sections()
        
        print("\n" + "="*60)
        print("  ABSCHNITTE")
        print("="*60)
        
        for section_info in sections:
            ending_marker = " [ENDE]" if section_info['is_ending'] else ""
            print(f"\n[{section_info['id']}] {section_info['title']}{ending_marker}")
            print(f"  Entscheidungen: {section_info['choices_count']}")
    
    def export_story(self):
        """Exportiert die Story"""
        if not self.manager.current_story:
            print("\nFehler: Keine Story geladen")
            return
        
        print("\n--- Story exportieren ---")
        print("1. Interaktives HTML (digitales Buch)")
        print("2. Druckbares HTML (Spielbuch)")
        print("3. Markdown")
        
        choice = input("\nFormat wählen (1-3): ").strip()
        
        exporter = StoryExporter(self.manager.current_story)
        
        try:
            if choice == "1":
                filename = input("Dateiname (z.B. story.html): ").strip()
                if not filename.endswith('.html'):
                    filename += '.html'
                exporter.export_to_html(filename, interactive=True)
                print(f"\n✓ Interaktives HTML exportiert: {filename}")
                print("  Öffne die Datei in einem Webbrowser zum Spielen!")
            
            elif choice == "2":
                filename = input("Dateiname (z.B. story_print.html): ").strip()
                if not filename.endswith('.html'):
                    filename += '.html'
                exporter.export_to_html(filename, interactive=False)
                print(f"\n✓ Druckbares HTML exportiert: {filename}")
                print("  Öffne die Datei in einem Webbrowser und drucke sie aus!")
            
            elif choice == "3":
                filename = input("Dateiname (z.B. story.md): ").strip()
                if not filename.endswith('.md'):
                    filename += '.md'
                exporter.export_to_markdown(filename)
                print(f"\n✓ Markdown exportiert: {filename}")
            
            else:
                print("Ungültige Auswahl")
        
        except Exception as e:
            print(f"Fehler beim Export: {e}")
    
    def load_example_zauberwald(self):
        """Lädt das Beispielprojekt Zauberwald"""
        example_path = "examples/zauberwald.json"
        
        if os.path.exists(example_path):
            try:
                self.manager.load_story(example_path)
                print(f"\n✓ Beispiel 'Zauberwald' wurde geladen!")
            except Exception as e:
                print(f"Fehler beim Laden: {e}")
        else:
            print(f"\nFehler: Beispieldatei nicht gefunden: {example_path}")
            print("Erstelle das Beispiel...")
            self._create_zauberwald_example()
    
    def _create_zauberwald_example(self):
        """Erstellt das Zauberwald-Beispiel"""
        # Erstelle examples Verzeichnis
        os.makedirs("examples", exist_ok=True)
        
        # Erstelle die Story
        story = self.manager.create_new_story(
            title="Der Zauberwald",
            description="Ein magisches Abenteuer für junge Entdecker",
            author="KI Book Builder"
        )
        
        # Abschnitt 1: Start
        self.manager.add_section(
            "S1",
            "Am Waldrand",
            "Du stehst am Rand eines geheimnisvollen Waldes. Die Bäume ragen hoch in den Himmel, und zwischen den Ästen funkeln magische Lichter. Ein schmaler Pfad führt tief in den Wald hinein, während rechts ein kristallklarer Bach plätschert."
        )
        
        self.manager.add_choice_to_section("S1", "Dem Pfad in den Wald folgen", "S2", "A")
        self.manager.add_choice_to_section("S1", "Dem Bach folgen", "S3", "B")
        
        # Abschnitt 2: Im Wald
        self.manager.add_section(
            "S2",
            "Im tiefen Wald",
            "Der Pfad führt dich tiefer in den Wald. Plötzlich siehst du eine kleine Fee, die auf einem Pilz sitzt. Sie winkt dir fröhlich zu."
        )
        
        self.manager.add_choice_to_section("S2", "Mit der Fee sprechen", "S4", "A")
        self.manager.add_choice_to_section("S2", "Weiter den Pfad entlang gehen", "S5", "B")
        
        # Abschnitt 3: Am Bach
        self.manager.add_section(
            "S3",
            "Der magische Bach",
            "Du folgst dem Bach und entdeckst eine wunderschöne Lichtung. In der Mitte steht ein alter Baum mit einer Tür im Stamm."
        )
        
        self.manager.add_choice_to_section("S3", "Die Tür öffnen", "S6", "A")
        self.manager.add_choice_to_section("S3", "Zurück zum Waldrand gehen", "S1", "B")
        
        # Abschnitt 4: Fee-Begegnung (Gutes Ende)
        self.manager.add_section(
            "S4",
            "Die Fee der Weisheit",
            "Die Fee lächelt dich an und schenkt dir einen magischen Kristall. 'Dieser wird dir immer den richtigen Weg zeigen', sagt sie. Du hast einen wertvollen Schatz gefunden!"
        )
        
        # Abschnitt 5: Verirrt (Neutrales Ende)
        self.manager.add_section(
            "S5",
            "Der endlose Pfad",
            "Du gehst weiter und weiter, doch der Pfad scheint kein Ende zu nehmen. Schließlich findest du einen Weg zurück zum Waldrand. Das Abenteuer war interessant, aber du hast nichts Besonderes gefunden."
        )
        
        # Abschnitt 6: Der Baumpalast (Großartiges Ende)
        self.manager.add_section(
            "S6",
            "Der verborgene Palast",
            "Die Tür öffnet sich und du betrittst einen prächtigen unterirdischen Palast! Die Waldgeister empfangen dich als ehrenvollen Gast. Du wirst zum Hüter des Zauberwaldes ernannt!"
        )
        
        # Speichere das Beispiel
        self.manager.save_story("examples/zauberwald.json")
        print("✓ Beispiel 'Zauberwald' wurde erstellt und gespeichert!")
    
    def run(self):
        """Startet die Hauptschleife"""
        print("\n🌟 Willkommen beim Interactive KI Book Builder! 🌟")
        
        while self.running:
            self.display_menu()
            choice = input("Wähle eine Option (0-9): ").strip()
            
            if choice == "1":
                self.create_new_story()
            elif choice == "2":
                self.load_story()
            elif choice == "3":
                self.save_story()
            elif choice == "4":
                self.add_section()
            elif choice == "5":
                self.add_choice()
            elif choice == "6":
                self.show_story_info()
            elif choice == "7":
                self.list_sections()
            elif choice == "8":
                self.export_story()
            elif choice == "9":
                self.load_example_zauberwald()
            elif choice == "0":
                print("\n👋 Auf Wiedersehen! Viel Spaß beim Geschichtenschreiben!\n")
                self.running = False
            else:
                print("\n⚠️  Ungültige Auswahl. Bitte wähle 0-9.")


def main():
    """Haupteinstiegspunkt"""
    # Prüfe ob --load Parameter übergeben wurde
    if len(sys.argv) > 2 and sys.argv[1] == "--load":
        filename = sys.argv[2]
        app = BookBuilder()
        
        if os.path.exists(filename):
            try:
                app.manager.load_story(filename)
                print(f"\n✓ Story '{filename}' wurde geladen!")
            except Exception as e:
                print(f"Fehler beim Laden: {e}")
        else:
            print(f"Fehler: Datei '{filename}' nicht gefunden")
        
        app.run()
    else:
        app = BookBuilder()
        app.run()


if __name__ == "__main__":
    main()
