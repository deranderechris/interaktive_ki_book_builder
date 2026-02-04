# Interaktiver KI Book Builder

Ein vollständiges Python-System zum Erstellen und Erleben interaktiver Geschichten mit KI-generierten Bildprompts.

## Features

✨ **Vollständiges Buchverwaltungssystem**
- Abschnitte/Szenen verwalten
- Entscheidungen speichern (A/B/C/D-Optionen)
- Multiple Enden für verschiedene Geschichtspfade

🧠 **Intelligentes Gedächtnissystem**
- Verfolgt besuchte Abschnitte
- Speichert alle getroffenen Entscheidungen
- Verwaltet Hinweise und offene Pfade
- Erstellt Zusammenfassungen des Spielverlaufs

🎨 **Automatische Bild-Prompt-Generierung**
- Generiert KI-Bildprompts für jede Szene
- Basiert auf Titel, Text und Atmosphäre
- Direkt kopierbar für KI-Bildgeneratoren (DALL-E, Midjourney, Stable Diffusion, etc.)
- Anpassbare Kunststile

💾 **JSON Import/Export**
- Speichern und Laden von Büchern im JSON-Format
- Speichern und Laden von Spielfortschritt
- Einfaches Teilen von Geschichten

🎮 **Interaktives CLI-Menü**
- Intuitive Navigation durch Geschichten
- Neue Geschichte starten oder fortsetzen
- Gedächtnis und Entscheidungshistorie anzeigen
- Spielstand speichern und laden

## Installation

### Voraussetzungen
- Python 3.7 oder höher

### Schritte

1. Repository klonen:
```bash
git clone https://github.com/deranderechris/interaktive_ki_book_builder.git
cd interaktive_ki_book_builder
```

2. (Optional) Virtuelle Umgebung erstellen:
```bash
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```

3. Das Projekt verwendet nur Python-Standardbibliotheken, keine zusätzlichen Abhängigkeiten nötig!

## Verwendung

### Beispielgeschichte spielen

```bash
python main.py
```

oder explizit:

```bash
python main.py examples/beispiel_buch.json
```

### Eigenes Buch verwenden

```bash
python main.py pfad/zu/deinem/buch.json
```

### Bild-Prompts generieren

Generiere automatisch Bild-Prompts für alle Abschnitte ohne vorhandene Prompts:

```bash
python main.py examples/beispiel_buch.json --generate-prompts
```

## Buchformat

Bücher werden im JSON-Format gespeichert. Hier ist ein Beispiel:

```json
{
  "title": "Meine Geschichte",
  "author": "Dein Name",
  "description": "Eine spannende Geschichte",
  "start_section_id": "start",
  "sections": {
    "start": {
      "id": "start",
      "title": "Der Anfang",
      "text": "Du stehst vor einer Tür...",
      "decisions": [
        {
          "option": "A",
          "text": "Tür öffnen",
          "next_section_id": "raum1"
        },
        {
          "option": "B",
          "text": "Umkehren",
          "next_section_id": "ende"
        }
      ],
      "is_ending": false,
      "image_prompt": "Scene: Der Anfang | Style: fantasy art..."
    },
    "raum1": {
      "id": "raum1",
      "title": "Ein mysteriöser Raum",
      "text": "Du betrittst einen dunklen Raum...",
      "decisions": [],
      "is_ending": true,
      "image_prompt": null
    }
  }
}
```

## Projektstruktur

```
interaktive_ki_book_builder/
├── main.py                    # Haupteinstiegspunkt
├── book_builder/              # Hauptpaket
│   ├── __init__.py
│   ├── models.py              # Datenmodelle (Book, Section, Decision, Memory)
│   ├── io.py                  # JSON Import/Export
│   ├── image_prompt.py        # Bild-Prompt-Generator
│   └── cli.py                 # CLI-Interface
├── examples/
│   └── beispiel_buch.json     # Beispielgeschichte
└── README.md
```

## CLI-Menü

Das interaktive Menü bietet folgende Optionen:

1. **Neue Geschichte starten** - Beginnt eine neue Geschichte vom Anfang
2. **Geschichte fortsetzen** - Setzt die aktuelle Geschichte fort
3. **Gedächtnis anzeigen** - Zeigt besuchte Abschnitte, Hinweise, offene Pfade und Zusammenfassung
4. **Entscheidungshistorie anzeigen** - Zeigt alle getroffenen Entscheidungen
5. **Fortschritt speichern** - Speichert den aktuellen Spielstand
6. **Fortschritt laden** - Lädt einen gespeicherten Spielstand
7. **Beenden** - Beendet das Programm

Während des Spiels:
- Wähle Optionen A, B, C oder D
- Drücke **M** um zum Hauptmenü zurückzukehren
- Drücke **G** um das Gedächtnis anzuzeigen

## Bild-Prompts

Für jeden Abschnitt wird automatisch ein KI-Bildprompt generiert, der:
- Den Titel der Szene enthält
- Einen Textausschnitt für Kontext liefert
- Die Atmosphäre basierend auf Schlüsselwörtern erkennt
- Im gewünschten Kunststil formatiert ist

Die Prompts sind so formatiert, dass sie direkt in KI-Bildgeneratoren wie DALL-E, Midjourney oder Stable Diffusion kopiert werden können.

Beispiel-Prompt:
```
Scene: Der Verzauberte Wald | Style: fantasy art, detailed illustration, high quality | Description: Du betrittst einen magischen Wald voller leuchtender Pilze... | Atmosphere: magical atmosphere, mystical, forest setting
```

## Eigene Geschichten erstellen

1. Erstelle eine neue JSON-Datei basierend auf dem Beispiel
2. Definiere Abschnitte mit eindeutigen IDs
3. Füge Entscheidungen hinzu, die auf andere Abschnitte verweisen
4. Markiere End-Abschnitte mit `"is_ending": true`
5. Lade dein Buch mit `python main.py dein_buch.json`

## Gedächtnissystem

Das Gedächtnissystem verfolgt:

- **Besuchte Abschnitte**: Alle Szenen, die du besucht hast
- **Getroffene Entscheidungen**: Historie aller Entscheidungen mit Reihenfolge
- **Hinweise**: Wichtige Informationen für den Spieler
- **Offene Pfade**: Noch nicht erkundete Möglichkeiten
- **Zusammenfassung**: Eine Übersicht über die Geschichte bisher

## Beispielgeschichte

Das mitgelieferte Beispiel "Das Abenteuer im Verzauberten Wald" bietet:
- 12 verschiedene Abschnitte
- 3 Startoptionen
- 9 verschiedene Enden
- Vollständig generierte Bild-Prompts
- Fantasy-Atmosphäre mit Magie und Geheimnissen

## Entwicklung

### Architektur

Das Projekt folgt einem modularen Design:
- **models.py**: Datenklassen mit Dataclasses
- **io.py**: Serialisierung/Deserialisierung
- **image_prompt.py**: KI-Prompt-Generierung
- **cli.py**: Benutzerinteraktion

### Erweiterungen

Mögliche Erweiterungen:
- Inventarsystem für Gegenstände
- Charakterattribute (Gesundheit, Magie, etc.)
- Zufallselemente und Würfelwürfe
- Mehrsprachige Unterstützung
- Grafische Benutzeroberfläche (GUI)
- Integration mit KI-APIs für dynamische Geschichten
- Multiplayer-Modi

## Lizenz

Dieses Projekt ist Open Source. Fühle dich frei, es zu verwenden, zu modifizieren und zu teilen!

## Autor

deranderechris

## Mitwirken

Beiträge sind willkommen! Fühle dich frei, Issues zu erstellen oder Pull Requests einzureichen.

---

Viel Spaß beim Erstellen deiner eigenen interaktiven Geschichten! 📚✨
