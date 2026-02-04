# Interactive KI Book Builder - Tutorial

Willkommen beim Interactive KI Book Builder! Dieses Tutorial zeigt dir, wie du dein eigenes interaktives Buch mit KI-generierten Bildern erstellen kannst.

## Inhaltsverzeichnis

1. [Installation](#installation)
2. [Erste Schritte](#erste-schritte)
3. [Erstellen einer Geschichte](#erstellen-einer-geschichte)
4. [Bilder generieren](#bilder-generieren)
5. [Erweiterte Optionen](#erweiterte-optionen)

## Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

### Schritte

1. Repository klonen oder herunterladen
2. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

3. Optional: OpenAI API Key konfigurieren (für Bildgenerierung)

Erstelle eine `.env` Datei im Hauptverzeichnis:

```
OPENAI_API_KEY=dein-api-key-hier
```

## Erste Schritte

### Beispiel ausführen

Probiere zunächst das mitgelieferte Beispiel aus:

```bash
python src/main.py examples/mini_gamebook.json --output mein_erstes_buch
```

Dies erstellt ein interaktives Buch im Verzeichnis `mein_erstes_buch`.

### Dein Buch anschauen

Öffne die generierte `book.html` Datei in deinem Browser:

```bash
# Linux/Mac
open mein_erstes_buch/book.html

# Windows
start mein_erstes_buch/book.html
```

## Erstellen einer Geschichte

### JSON-Format

Geschichten werden im JSON-Format definiert. Hier ist die grundlegende Struktur:

```json
{
  "title": "Titel deiner Geschichte",
  "author": "Dein Name",
  "description": "Eine kurze Beschreibung",
  "pages": [
    {
      "id": "start",
      "text": "Dies ist der Text auf der ersten Seite.",
      "image_prompt": "Beschreibung für das KI-generierte Bild",
      "choices": [
        {
          "text": "Erste Wahlmöglichkeit",
          "next": "seite_2"
        },
        {
          "text": "Zweite Wahlmöglichkeit",
          "next": "seite_3"
        }
      ]
    }
  ]
}
```

### Wichtige Felder

- **title**: Der Titel deines Buches (Pflichtfeld)
- **pages**: Liste aller Seiten (Pflichtfeld)
  - **id**: Eindeutige ID für die Seite (Pflichtfeld)
  - **text**: Der Text, der auf der Seite angezeigt wird (Pflichtfeld)
  - **image_prompt**: Beschreibung für das zu generierende Bild (optional)
  - **choices**: Liste von Wahlmöglichkeiten (optional)
    - **text**: Text der Wahlmöglichkeit
    - **next**: ID der nächsten Seite

### Tipps für gute Geschichten

1. **Klare Struktur**: Beginne mit einer Start-Seite (id: "start")
2. **Sinnvolle Verzweigungen**: Jede Wahl sollte zu unterschiedlichen Ergebnissen führen
3. **Endpunkte**: Erstelle mehrere mögliche Enden für deine Geschichte
4. **Beschreibende Texte**: Nutze lebendige Beschreibungen, um die Fantasie anzuregen

## Bilder generieren

### Mit KI-Bildern

Um Bilder mit OpenAI DALL-E zu generieren, brauchst du:

1. Einen OpenAI API Key
2. Den `image_prompt` für jede Seite

```bash
python src/main.py deine_geschichte.json --output ausgabe
```

### Ohne Bilder

Falls du keine Bilder generieren möchtest:

```bash
python src/main.py deine_geschichte.json --output ausgabe --no-images
```

### Eigene Bilder verwenden

Du kannst auch eigene Bilder einbinden, indem du das `image` Feld direkt setzt:

```json
{
  "id": "start",
  "text": "...",
  "image": "pfad/zu/deinem/bild.png"
}
```

## Erweiterte Optionen

### Kommandozeilen-Optionen

```bash
python src/main.py --help
```

Zeigt alle verfügbaren Optionen:

- `--output`, `-o`: Ausgabeverzeichnis
- `--no-images`: Bilder nicht generieren
- `--verbose`, `-v`: Ausführliche Ausgabe

### Konfiguration

Erstelle eine `config.json` im Hauptverzeichnis für erweiterte Einstellungen:

```json
{
  "openai_api_key": "dein-api-key",
  "image_model": "dall-e-3",
  "image_size": "1024x1024"
}
```

## Beispiele

### Einfache lineare Geschichte

Eine Geschichte ohne Verzweigungen:

```json
{
  "title": "Eine einfache Geschichte",
  "pages": [
    {
      "id": "start",
      "text": "Es war einmal...",
      "choices": [{"text": "Weiter", "next": "page2"}]
    },
    {
      "id": "page2",
      "text": "...ein tapferer Held.",
      "choices": [{"text": "Weiter", "next": "end"}]
    },
    {
      "id": "end",
      "text": "Ende."
    }
  ]
}
```

### Verzweigte Geschichte

Eine Geschichte mit mehreren Enden:

```json
{
  "title": "Die Wahl",
  "pages": [
    {
      "id": "start",
      "text": "Du kommst an eine Kreuzung.",
      "choices": [
        {"text": "Links gehen", "next": "left"},
        {"text": "Rechts gehen", "next": "right"}
      ]
    },
    {
      "id": "left",
      "text": "Du findest einen Schatz!"
    },
    {
      "id": "right",
      "text": "Du verläufst dich..."
    }
  ]
}
```

## Fehlerbehebung

### Häufige Probleme

**Problem**: `FileNotFoundError`
- **Lösung**: Überprüfe, ob der Pfad zur JSON-Datei korrekt ist

**Problem**: `JSONDecodeError`
- **Lösung**: Validiere deine JSON-Datei (z.B. mit jsonlint.com)

**Problem**: Bilder werden nicht generiert
- **Lösung**: Überprüfe deinen OpenAI API Key in der `.env` Datei

## Weitere Ressourcen

- [OpenAI API Dokumentation](https://platform.openai.com/docs)
- [JSON Tutorial](https://www.json.org/json-de.html)
- [Python Dokumentation](https://docs.python.org/3/)

## Support

Bei Fragen oder Problemen öffne bitte ein Issue auf GitHub.

Viel Spaß beim Erstellen deiner interaktiven Bücher! 📚✨
