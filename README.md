# Interaktiver KI Book Builder

Hiermit kann jeder sein eigenes interaktives Buch mit Bildern erstellen!

## Beschreibung

Der Interaktive Book Builder ist ein einfaches Python-Tool, mit dem Sie schnell und einfach interaktive Bücher erstellen können. Sie können Kapitel hinzufügen, Bilder einbinden und Ihr Buch in verschiedenen Formaten (JSON, HTML) exportieren.

## Features

- ✨ Einfaches Erstellen von Büchern mit Kapiteln
- 🖼️ Unterstützung für Bilder in jedem Kapitel
- 💾 Export als JSON-Datei
- 🌐 Export als HTML-Datei (schön formatiert und sofort im Browser ansehbar)
- 📝 Vollständig in Python geschrieben (keine externen Abhängigkeiten)

## Installation

1. Repository klonen:
```bash
git clone https://github.com/deranderechris/interaktive_ki_book_builder.git
cd interaktive_ki_book_builder
```

2. Python 3.6 oder höher ist erforderlich (keine zusätzlichen Pakete notwendig)

## Verwendung

### Schnellstart mit Beispiel

Führen Sie einfach das Beispiel-Skript aus:

```bash
python3 example.py
```

Dies erstellt ein Beispielbuch mit mehreren Kapiteln und speichert es als `zeitreise_buch.json` und `zeitreise_buch.html`.

### Eigenes Buch erstellen

Erstellen Sie eine neue Python-Datei (z.B. `mein_buch.py`):

```python
from book_builder import InteractivBook

# Neues Buch erstellen
book = InteractivBook(
    title="Mein Buch-Titel",
    author="Ihr Name"
)

# Kapitel hinzufügen
book.add_chapter(
    chapter_title="Erstes Kapitel",
    content="Dies ist der Inhalt des ersten Kapitels...",
    image_path="pfad/zum/bild.jpg"  # Optional
)

book.add_chapter(
    chapter_title="Zweites Kapitel",
    content="Hier kommt der Inhalt des zweiten Kapitels..."
)

# Buch speichern
book.save_to_json("mein_buch.json")
book.save_to_html("mein_buch.html")
```

### Direkte Verwendung

Sie können auch direkt mit dem `book_builder.py` arbeiten:

```bash
python3 book_builder.py
```

Dies führt ein Beispiel aus und zeigt die grundlegende Funktionalität.

## API-Referenz

### InteractivBook-Klasse

#### `__init__(title: str, author: str)`
Erstellt ein neues Buch.

#### `add_chapter(chapter_title: str, content: str, image_path: str = None)`
Fügt ein neues Kapitel zum Buch hinzu.

#### `save_to_json(filename: str = "book.json")`
Speichert das Buch als JSON-Datei.

#### `save_to_html(filename: str = "book.html")`
Speichert das Buch als formatierte HTML-Datei.

#### `display_info()`
Zeigt Informationen über das Buch in der Konsole an.

## Beispiel-Ausgabe

Nach dem Ausführen wird eine HTML-Datei erstellt, die Sie direkt in Ihrem Browser öffnen können. Das Buch wird mit einem schönen, lesbaren Design angezeigt.

## Lizenz

Dieses Projekt ist Open Source und frei verfügbar.

## Beiträge

Beiträge sind willkommen! Fühlen Sie sich frei, Issues zu erstellen oder Pull Requests einzureichen.

## Autor

Chris (deranderechris)
