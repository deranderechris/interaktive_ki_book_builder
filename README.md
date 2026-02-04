# Interaktiver KI Book Builder

Ein Python-basiertes Tool zum Erstellen und Spielen von interaktiven Büchern (Gamebooks) mit Bildern und verzweigten Geschichten.

## Beschreibung

Mit dem Interaktiven KI Book Builder kann jeder sein eigenes interaktives Buch mit Bildern erstellen. Das System ermöglicht es, verzweigte Geschichten zu entwickeln, bei denen Leser Entscheidungen treffen können, die den Verlauf der Geschichte beeinflussen.

## Installation

### Voraussetzungen

- Python 3.6 oder höher
- Keine zusätzlichen Abhängigkeiten erforderlich (nur Python-Standardbibliothek)

### Einrichtung

1. Repository klonen:
```bash
git clone https://github.com/deranderechris/interaktive_ki_book_builder.git
cd interaktive_ki_book_builder
```

2. Das war's! Das Projekt ist sofort einsatzbereit.

## Verwendung

### Beispiel starten

Um ein vorhandenes Gamebook zu spielen:

```bash
python src/main.py --example examples/mini_gamebook.json
```

### Hilfe anzeigen

```bash
python src/main.py --help
```

### Eigenes Gamebook erstellen

Erstellen Sie eine JSON-Datei mit folgendem Format:

```json
{
  "title": "Titel Ihrer Geschichte",
  "description": "Eine kurze Beschreibung Ihrer Geschichte",
  "start_scene": "start",
  "scenes": [
    {
      "id": "start",
      "title": "Der Anfang",
      "text": "Dies ist der erste Abschnitt Ihrer Geschichte...",
      "image": "bild1.jpg",
      "choices": [
        {
          "text": "Wähle Option 1",
          "next_scene": "szene2"
        },
        {
          "text": "Wähle Option 2",
          "next_scene": "szene3"
        }
      ]
    }
  ]
}
```

### JSON-Format Erklärung

#### Hauptstruktur
- `title` (string): Der Titel Ihres Gamebooks
- `description` (string, optional): Eine Beschreibung der Geschichte
- `start_scene` (string): Die ID der Startszene
- `scenes` (array): Liste aller Szenen in Ihrer Geschichte

#### Szenen-Struktur
Jede Szene enthält:
- `id` (string): Eindeutige Kennung für die Szene
- `title` (string): Titel der Szene
- `text` (string): Der Textinhalt der Szene
- `image` (string, optional): Dateiname oder Pfad zu einem Bild
- `choices` (array): Liste der verfügbaren Auswahlmöglichkeiten
  - Leer lassen für ein Ende der Geschichte

#### Auswahl-Struktur
Jede Auswahl enthält:
- `text` (string): Der anzuzeigende Text für die Auswahl
- `next_scene` (string): ID der nächsten Szene
  - Kann `null` sein für ein Geschichtsende

## Beispiele

Das Repository enthält Beispiel-Gamebooks im `examples/` Verzeichnis:

- `mini_gamebook.json` - Ein kleines interaktives Abenteuer zum Testen
  - Zeigt verschiedene Verzweigungen und Enden
  - Demonstriert die Verwendung von Bildreferenzen
  - Vollständig auf Deutsch

## Funktionen

- ✨ Verzweigte, interaktive Geschichten
- 🎨 Unterstützung für Bildreferenzen in jeder Szene
- 🎮 Einfache, textbasierte Benutzeroberfläche
- 📝 Einfaches JSON-Format für Geschichten
- 🌍 Vollständig auf Deutsch
- 🚀 Keine externen Abhängigkeiten erforderlich

## Beitragen

Beiträge sind willkommen! Wenn Sie Verbesserungen oder neue Funktionen hinzufügen möchten:

1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/NeuesFunktion`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Füge neue Funktion hinzu'`)
4. Pushen Sie zum Branch (`git push origin feature/NeuesFunktion`)
5. Erstellen Sie einen Pull Request

## Lizenz

Dieses Projekt ist Open Source und für jeden frei verwendbar.

## Autor

deranderechris

## Kontakt

Bei Fragen oder Anregungen können Sie ein Issue im GitHub-Repository erstellen.
