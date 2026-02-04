# Interactive KI Book Builder

Ein interaktiver KI-Book-Builder für personalisierte Geschichten, Spielbücher und Kinderabenteuer.

Mit diesem Tool kannst du deine eigene interaktive Geschichte erstellen, Abschnitte, Entscheidungen und KI-generierte Bild-Prompts direkt einbinden.

## Features

- Erstellung von interaktiven Geschichten mit Abschnitten und Entscheidungen
- Unterstützung von Multiple-Choice-Entscheidungen (A/B/C/D)
- Speicherung von Story-Gedächtnis, Hinweisen und offenen Pfaden
- Automatische Generierung von Bild-Prompts für jede Szene
- Export als druckbares Spielbuch oder digitales interaktives Buch
- Beispielprojekt: Mini-Spielbuch „Zauberwald"

## Installation

```bash
git clone https://github.com/deranderechris/interaktive_ki_book_builder.git
cd interaktive_ki_book_builder
pip install -r requirements.txt
```

## Verwendung

```bash
python book_builder.py
```

Das Programm bietet ein interaktives Menü zur Erstellung und Verwaltung deiner interaktiven Geschichten.

### Beispielprojekt laden

Um das Beispielprojekt "Zauberwald" zu laden:

```bash
python book_builder.py --load examples/zauberwald.json
```

## Projektstruktur

```
interaktive_ki_book_builder/
├── book_builder.py          # Hauptanwendung
├── story_manager.py         # Story-Verwaltung
├── models.py                # Datenmodelle (Section, Choice, Story)
├── image_prompt_generator.py # KI-Bild-Prompt-Generator
├── exporter.py              # Export-Funktionalität
├── requirements.txt         # Python-Abhängigkeiten
├── README.md                # Diese Datei
└── examples/
    └── zauberwald.json      # Beispielgeschichte
```

## Lizenz

MIT License
