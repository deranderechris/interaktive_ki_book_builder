# interaktive_ki_book_builder
hiermit kann jeder sein eigenes interaktives Buch mit Bildern erstellen

## Beschreibung

Ein interaktiver Spielbuch-Builder, mit dem du deine eigenen verzweigten Geschichten mit Entscheidungen und verschiedenen Enden erstellen und spielen kannst.

## Installation

Keine zusätzlichen Abhängigkeiten erforderlich - verwendet nur Python Standard-Bibliotheken.

Voraussetzungen:
- Python 3.7 oder höher

## Verwendung

### Spielen eines vorhandenen Spielbuchs

```bash
python3 src/main.py
```

Wenn du aufgefordert wirst, gib den Pfad zu deinem Spielbuch ein (z.B. `examples/mini_gamebook.json`).

### Erstellen deines eigenen Spielbuchs

Erstelle eine JSON-Datei mit folgender Struktur:

```json
{
  "title": "Dein Titel",
  "description": "Deine Beschreibung",
  "start": "start_node_id",
  "nodes": {
    "start_node_id": {
      "text": "Der Text, der dem Spieler angezeigt wird",
      "image": "optionaler_bildpfad.jpg",
      "choices": [
        {
          "text": "Erste Wahl",
          "next": "node_id_für_diese_wahl"
        },
        {
          "text": "Zweite Wahl",
          "next": "anderer_node_id"
        }
      ]
    },
    "ende_node": {
      "text": "Ende der Geschichte",
      "image": "optionales_bild.jpg",
      "end": true,
      "ending_message": "Nachricht am Ende"
    }
  }
}
```

### Beispiel

Ein vollständiges Beispiel findest du in `examples/mini_gamebook.json` - eine kurze Geschichte über eine verzauberte Bibliothek.

## Projektstruktur

```
.
├── src/
│   ├── main.py           # Haupteinstiegspunkt der Anwendung
│   └── story_manager.py  # Kernlogik für Story-Management
├── examples/
│   └── mini_gamebook.json # Beispiel-Spielbuch
└── README.md
```

## Features

- ✅ Verzweigte narrative Strukturen
- ✅ Mehrere Enden
- ✅ Bildunterstützung (Referenzen in der Story-Struktur)
- ✅ Benutzerfreundliche Auswahl-Schnittstelle
- ✅ Fehlerbehandlung für ungültige Eingaben
- ✅ Einfaches JSON-Format für Story-Dateien
