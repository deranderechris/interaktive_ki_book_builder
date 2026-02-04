# Interactive KI Book Builder

Erstelle dein eigenes interaktives Buch mit KI-generierten Bildern! 📚✨

## Überblick

Der Interactive KI Book Builder ist ein Python-Tool, mit dem du interaktive Geschichten (Gamebooks) erstellen kannst. Die Geschichten können mit KI-generierten Bildern illustriert werden und werden als HTML-Dateien exportiert, die direkt im Browser geöffnet werden können.

## Features

- 📖 Erstelle verzweigte, interaktive Geschichten
- 🎨 Generiere Bilder automatisch mit OpenAI DALL-E
- 🌐 Exportiere als HTML für einfaches Teilen
- 📝 Einfaches JSON-basiertes Story-Format
- 🇩🇪 Deutsche Benutzeroberfläche

## Projektstruktur

```
Interactive-KI-Book-Builder/
│
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── main.py              # Haupteinstiegspunkt
│   ├── story_manager.py     # Verwaltung der Geschichten
│   ├── image_generator.py   # KI-Bildgenerierung
│   └── utils.py             # Hilfsfunktionen
├── examples/
│   └── mini_gamebook.json   # Beispielgeschichte
└── docs/
    └── tutorial.md          # Ausführliches Tutorial
```

## Schnellstart

### Installation

```bash
# Repository klonen
git clone https://github.com/deranderechris/interaktive_ki_book_builder.git
cd interaktive_ki_book_builder

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### Verwendung

```bash
# Beispielgeschichte generieren
python src/main.py examples/mini_gamebook.json --output mein_buch

# Ohne Bildgenerierung
python src/main.py examples/mini_gamebook.json --output mein_buch --no-images
```

### Das Ergebnis anschauen

Öffne die generierte `book.html` Datei im Browser:

```bash
# Linux/Mac
open mein_buch/book.html

# Windows
start mein_buch/book.html
```

## Beispiel-Story-Format

```json
{
  "title": "Mein Abenteuer",
  "pages": [
    {
      "id": "start",
      "text": "Du stehst vor einer Tür...",
      "image_prompt": "Eine mysteriöse Tür in einem alten Gebäude",
      "choices": [
        {"text": "Tür öffnen", "next": "room"},
        {"text": "Weggehen", "next": "end"}
      ]
    },
    {
      "id": "room",
      "text": "Du betrittst einen großen Raum..."
    },
    {
      "id": "end",
      "text": "Du gehst nach Hause."
    }
  ]
}
```

## Dokumentation

Für eine ausführliche Anleitung siehe [Tutorial](docs/tutorial.md).

## Konfiguration (Optional)

Für die Bildgenerierung benötigst du einen OpenAI API Key. Erstelle eine `.env` Datei:

```
OPENAI_API_KEY=dein-api-key-hier
```

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## Mitwirken

Contributions sind willkommen! Öffne gerne Issues oder Pull Requests.

## Autor

deranderechris

---

Viel Spaß beim Erstellen deiner eigenen interaktiven Geschichten! 🚀
