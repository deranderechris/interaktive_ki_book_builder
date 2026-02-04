# 📖 Interaktiver KI-Geschichten-Builder

Hiermit kann jeder sein eigenes interaktives Buch mit Bildern erstellen!

## 🚀 Schnellstart

1. Öffne `index.html` in deinem Browser
2. Lade die `example-story.json` Datei
3. Erlebe dein interaktives Abenteuer!

## 📝 Eigene Geschichten erstellen

### JSON-Struktur

Erstelle eine neue JSON-Datei mit folgender Struktur:

```json
{
  "title": "Titel deiner Geschichte",
  "description": "Kurze Beschreibung",
  "author": "Dein Name",
  "startSection": "start",
  "sections": {
    "start": {
      "text": "Der Text deines ersten Abschnitts...",
      "imagePrompt": "Beschreibung für KI-Bildgenerierung",
      "choices": [
        {
          "id": "A",
          "text": "Erste Entscheidung",
          "nextSection": "section2"
        },
        {
          "id": "B",
          "text": "Zweite Entscheidung",
          "nextSection": "section3"
        }
      ]
    }
  }
}
```

### Jeder Abschnitt enthält:

1. **text** (erforderlich): Der Textinhalt des Abschnitts
2. **imagePrompt** (erforderlich): Prompt für die Bildgenerierung mit KI
3. **choices** (optional): Array von Entscheidungsmöglichkeiten (A/B/C/D)
   - **id**: Buchstabe A, B, C oder D
   - **text**: Beschreibung der Entscheidung
   - **nextSection**: ID des nächsten Abschnitts oder "END"
4. **isEnding** (optional): `true` wenn dies ein Endabschnitt ist

## 🎯 Features

- ✅ Interaktive Entscheidungsmöglichkeiten (A/B/C/D)
- ✅ Unbegrenzte Anzahl von Abschnitten und Pfaden
- ✅ Bild-Prompts für KI-Generierung
- ✅ Mehrere mögliche Enden
- ✅ Pfad-Tracker zeigt deinen Weg durch die Geschichte
- ✅ Responsive Design für alle Geräte
- ✅ Schöne, moderne Benutzeroberfläche

## 📦 Dateien

- `index.html` - Der interaktive Story-Builder/Viewer
- `story-schema.json` - JSON-Schema zur Validierung
- `example-story.json` - Beispielgeschichte "Das Magische Abenteuer"

## 🎨 Bild-Prompts

Die `imagePrompt`-Felder in deiner JSON-Datei sind ideal für KI-Bildgenerierung mit Tools wie:
- DALL-E
- Midjourney
- Stable Diffusion
- Andere KI-Bildgeneratoren

## 💡 Tipps für gute Geschichten

1. **Verzweigungen planen**: Zeichne ein Diagramm deiner Geschichte
2. **Klare Entscheidungen**: Jede Wahl sollte bedeutungsvoll sein
3. **Mehrere Enden**: Gib verschiedene Ausgänge für unterschiedliche Pfade
4. **Gute Bild-Prompts**: Beschreibe Szenen detailliert für bessere KI-Bilder
5. **Testen**: Spiele alle Pfade durch, um sicherzustellen, dass alles funktioniert

## 🔧 Technische Details

- Reine HTML/CSS/JavaScript - keine Installation nötig
- Funktioniert offline nach dem ersten Laden
- JSON-basiert für einfache Erstellung und Bearbeitung
- Validierung gegen JSON-Schema möglich

## 📄 Lizenz

Dieses Projekt kann frei verwendet und modifiziert werden.
