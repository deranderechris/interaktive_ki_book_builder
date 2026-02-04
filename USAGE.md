# Verwendungsanleitung - Interaktiver KI Book Builder

## Schnellstart

### Eine Geschichte spielen

1. Starte das Programm:
```bash
python main.py
```

2. Wähle im Hauptmenü Option **[1] Neue Geschichte starten**

3. Lese die Szene und wähle eine Entscheidung (A, B, C oder D)

4. Navigiere durch die Geschichte bis zu einem Ende

### Tastenbefehle während des Spiels

- **A, B, C, D**: Wähle eine der verfügbaren Optionen
- **M**: Zurück zum Hauptmenü
- **G**: Zeige das Gedächtnis an (besuchte Abschnitte, Hinweise, etc.)

## Hauptmenü-Optionen

### [1] Neue Geschichte starten
Beginnt eine komplett neue Geschichte vom Startpunkt. Löscht alle bisherigen Fortschritte im aktuellen Spiel.

### [2] Geschichte fortsetzen
Setzt die aktuelle Geschichte vom letzten Punkt fort. Verwende dies, nachdem du zum Hauptmenü zurückgekehrt bist.

### [3] Gedächtnis anzeigen
Zeigt detaillierte Informationen über deinen Spielfortschritt:
- Anzahl besuchter Abschnitte
- Anzahl getroffener Entscheidungen
- Gesammelte Hinweise
- Offene Pfade, die du noch erkunden kannst
- Zusammenfassung deiner bisherigen Reise

### [4] Entscheidungshistorie anzeigen
Zeigt eine chronologische Liste aller Entscheidungen, die du getroffen hast:
```
1. Der Beginn des Abenteuers: Option A
2. Im Herzen des Waldes: Option C
3. ...
```

### [5] Fortschritt speichern
Speichert deinen aktuellen Spielstand in eine JSON-Datei:
1. Wähle Option [5]
2. Gib einen Dateinamen ein (z.B. `mein_spielstand.json`)
3. Der Fortschritt wird gespeichert

Die Datei enthält:
- Alle besuchten Abschnitte
- Alle getroffenen Entscheidungen
- Gesammelte Hinweise
- Offene Pfade
- Zusammenfassung
- Aktueller Abschnitt

### [6] Fortschritt laden
Lädt einen zuvor gespeicherten Spielstand:
1. Wähle Option [6]
2. Gib den Dateinamen des Speicherstands ein
3. Dein Fortschritt wird wiederhergestellt

### [7] Beenden
Beendet das Programm. **Achtung**: Nicht gespeicherte Fortschritte gehen verloren!

## Bild-Prompts verwenden

Jeder Abschnitt zeigt einen KI-Bildprompt im Format:

```
📸 BILD-PROMPT (kopierbar):
--------------------------------------------------------------------------------
Scene: Der Titel | Style: fantasy art, detailed illustration, high quality | 
Description: Eine Beschreibung der Szene... | 
Atmosphere: magical atmosphere, mystical
--------------------------------------------------------------------------------
```

### So verwendest du die Prompts:

1. **Kopiere den gesamten Prompt** (alles zwischen den Trennlinien)

2. **Füge ihn in einen KI-Bildgenerator ein**:
   - DALL-E (OpenAI)
   - Midjourney (Discord)
   - Stable Diffusion
   - Leonardo.ai
   - Bing Image Creator

3. **Generiere das Bild** und visualisiere deine Geschichte!

### Prompt-Komponenten:

- **Scene**: Der Titel der Szene
- **Style**: Der Kunststil (standardmäßig Fantasy Art)
- **Description**: Kontext aus dem Text der Szene
- **Atmosphere**: Automatisch erkannte Stimmung (dunkel, magisch, friedlich, etc.)

## Eigene Bücher erstellen

### 1. JSON-Datei erstellen

Erstelle eine neue Datei, z.B. `mein_buch.json`:

```json
{
  "title": "Mein Abenteuer",
  "author": "Dein Name",
  "description": "Eine spannende Geschichte",
  "start_section_id": "start",
  "sections": {
    "start": {
      "id": "start",
      "title": "Der Anfang",
      "text": "Deine Geschichte beginnt hier...",
      "decisions": [
        {
          "option": "A",
          "text": "Option A beschreibung",
          "next_section_id": "naechster_abschnitt"
        }
      ],
      "is_ending": false,
      "image_prompt": null
    }
  }
}
```

### 2. Wichtige Regeln

- Jeder Abschnitt braucht eine **eindeutige ID**
- Die `start_section_id` muss auf einen existierenden Abschnitt zeigen
- `next_section_id` in Entscheidungen muss auf existierende Abschnitte verweisen
- End-Abschnitte haben `"is_ending": true` und eine leere `decisions`-Liste
- Optionen sollten A, B, C oder D sein

### 3. Buch laden

```bash
python main.py mein_buch.json
```

### 4. Bild-Prompts generieren

Lass automatisch Prompts für alle Abschnitte ohne Prompt erstellen:

```bash
python main.py mein_buch.json --generate-prompts
```

Dies überschreibt die Datei und fügt Prompts hinzu.

## Tipps und Tricks

### Mehrere Spielstände verwalten

Erstelle verschiedene Speicherdateien für verschiedene Pfade:
- `wald_pfad.json`
- `dorf_pfad.json`
- `nacht_pfad.json`

### Buch-Struktur planen

1. **Mind Map erstellen**: Zeichne alle möglichen Pfade
2. **IDs vergeben**: Nutze sprechende Namen (`wald_1`, `kampf_drache`, etc.)
3. **Enden planen**: Mindestens 3-5 verschiedene Enden
4. **Testen**: Spiele alle Pfade durch!

### Atmosphäre-Schlüsselwörter

Der Prompt-Generator erkennt diese Wörter im Text:
- `dunkel` → dark atmosphere
- `hell` → bright atmosphere
- `wald` → forest setting
- `stadt` → urban setting
- `gefahr` → dangerous atmosphere
- `frieden` → peaceful atmosphere
- `magie` → magical atmosphere
- `kampf` → battle scene
- `schloss` → castle setting
- `höhle` → cave setting

Verwende diese Wörter in deinen Texten für bessere Prompts!

## Beispiel-Spieldurchlauf

```
1. Starte: python main.py
2. Wähle: [1] Neue Geschichte
3. Lese: "Der Beginn des Abenteuers"
4. Wähle: A (Waldpfad)
5. Lese: "Im Herzen des Waldes"
6. Drücke: G (Gedächtnis anzeigen)
7. Wähle: C (Flüstern lauschen)
8. Lese: "Das Flüstern der Bäume" (Ende)
9. Drücke: Enter (Zurück zum Menü)
10. Wähle: [5] Fortschritt speichern
11. Eingabe: wald_ende.json
12. Wähle: [7] Beenden
```

## Fehlerbehebung

### "Datei nicht gefunden"
- Prüfe, ob die JSON-Datei existiert
- Verwende den vollständigen Pfad: `python main.py /pfad/zur/datei.json`

### "Abschnitt nicht gefunden"
- Prüfe, ob alle `next_section_id` auf existierende IDs verweisen
- Prüfe die `start_section_id` im Buch

### "Invalid JSON"
- Validiere deine JSON-Datei mit einem Online-Validator
- Achte auf fehlende Kommas, Klammern, Anführungszeichen

### Encoding-Probleme
- Speichere JSON-Dateien immer in UTF-8
- Deutsche Umlaute sollten funktionieren (ä, ö, ü, ß)

## Fortgeschrittene Nutzung

### Programmatisch Bücher erstellen

```python
from book_builder.models import Book, Section, Decision
from book_builder.io import BookIO

# Buch erstellen
book = Book(
    title="Mein Buch",
    author="Ich",
    description="Beschreibung",
    start_section_id="start"
)

# Abschnitte erstellen
start = Section(
    id="start",
    title="Anfang",
    text="Text...",
    decisions=[
        Decision(option="A", text="Wähle A", next_section_id="ende")
    ]
)

ende = Section(
    id="ende",
    title="Ende",
    text="Das Ende",
    is_ending=True
)

# Zum Buch hinzufügen
book.add_section(start)
book.add_section(ende)

# Speichern
BookIO.save_book(book, "mein_buch.json")
```

### Eigene Prompt-Stile

Momentan ist der Stil fest auf "fantasy art" gesetzt. Du kannst dies in `book_builder/image_prompt.py` ändern oder erweitern.

## Support

Bei Fragen oder Problemen:
1. Prüfe diese Dokumentation
2. Schaue dir das Beispielbuch an (`examples/beispiel_buch.json`)
3. Erstelle ein Issue auf GitHub

Viel Spaß beim Erstellen und Spielen deiner interaktiven Geschichten! 🎮📚
