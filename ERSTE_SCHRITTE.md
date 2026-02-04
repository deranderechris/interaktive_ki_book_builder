# 📚 Erste Schritte - Einsteigerfreundliche Anleitung

Willkommen beim Interaktiven KI Book Builder! Diese Anleitung führt dich Schritt für Schritt durch die Installation und Nutzung des Programms. Perfekt für alle, die gerade erst anfangen!

## 🎯 Was ist der Interaktive KI Book Builder?

Mit diesem Tool kannst du ganz einfach eigene interaktive Bücher mit Text und Bildern erstellen. Du brauchst keine Vorkenntnisse - folge einfach dieser Anleitung!

## 📥 Download und Installation

### Schritt 1: Herunterladen

Es gibt mehrere Möglichkeiten, den Book Builder zu erhalten:

#### Option A: Als ZIP herunterladen (am einfachsten)
1. Gehe zur GitHub-Seite: https://github.com/deranderechris/interaktive_ki_book_builder
2. Klicke auf den grünen Button "Code"
3. Wähle "Download ZIP"
4. Entpacke die ZIP-Datei auf deinem Computer

#### Option B: Mit Git klonen (für Fortgeschrittene)
```bash
git clone https://github.com/deranderechris/interaktive_ki_book_builder.git
cd interaktive_ki_book_builder
```

### Schritt 2: Python überprüfen

Der Book Builder benötigt Python 3.x. Überprüfe, ob Python installiert ist:

**Auf Windows:**
1. Öffne die Eingabeaufforderung (CMD)
2. Tippe ein: `python --version` oder `python3 --version`

**Auf Mac/Linux:**
1. Öffne das Terminal
2. Tippe ein: `python3 --version`

Du solltest etwas wie "Python 3.8.0" oder höher sehen.

**Falls Python nicht installiert ist:**
- Gehe zu https://www.python.org/downloads/
- Lade die neueste Version herunter
- Installiere sie (wichtig: Setze den Haken bei "Add Python to PATH")

### Schritt 3: Dateien prüfen

Navigiere zum heruntergeladenen Ordner und überprüfe, dass folgende Dateien vorhanden sind:
- `book_builder.py` - Das Hauptprogramm
- `test_book_builder.py` - Testprogramm
- `README.md` - Allgemeine Dokumentation
- `ERSTE_SCHRITTE.md` - Diese Anleitung

## 🚀 Dein erstes Buch erstellen

### Methode 1: Das Beispielbuch ausprobieren (empfohlen für den Start)

Das ist der einfachste Weg, um zu sehen, wie alles funktioniert:

1. Öffne die Eingabeaufforderung (Windows) oder das Terminal (Mac/Linux)
2. Navigiere zum Projektordner:
   ```bash
   cd Pfad/zum/interaktive_ki_book_builder
   ```
3. Führe das Beispiel aus:
   ```bash
   python3 book_builder.py
   ```

Du solltest ein Beispielbuch über einen kleinen Frosch sehen! 🐸

### Methode 2: Dein eigenes Buch schreiben

Jetzt wird's spannend! Erstelle dein eigenes Buch:

#### Schritt-für-Schritt Anleitung:

1. **Erstelle eine neue Python-Datei**
   - Öffne einen Texteditor (z.B. Notepad, TextEdit, oder Visual Studio Code)
   - Speichere die Datei als `mein_buch.py` im gleichen Ordner

2. **Schreibe den Code** (kopiere diesen Text in deine Datei):

```python
# Importiere das Book Builder Tool
from book_builder import InteractiveBook

# Erstelle ein neues Buch mit einem Titel
mein_buch = InteractiveBook("Meine Abenteuergeschichte")

# Füge die erste Seite hinzu
mein_buch.add_page(
    "Es war einmal an einem sonnigen Tag...",
    "bild1.jpg"  # Optional: Bildpfad
)

# Füge weitere Seiten hinzu
mein_buch.add_page(
    "Das Abenteuer beginnt!",
    "bild2.jpg"
)

mein_buch.add_page(
    "Und sie lebten glücklich bis ans Ende ihrer Tage.",
    "bild3.jpg"
)

# Zeige das gesamte Buch an
mein_buch.display_all()
```

3. **Führe dein Buch aus**
   ```bash
   python3 mein_buch.py
   ```

🎉 Herzlichen Glückwunsch! Du hast dein erstes interaktives Buch erstellt!

## 💡 Tipps und Tricks für Einsteiger

### Bilder hinzufügen

Du kannst echte Bilder verwenden:
1. Lege deine Bilder in den gleichen Ordner wie deine Python-Datei
2. Gib den Dateinamen beim Erstellen der Seite an
3. Beispiel: `mein_buch.add_page("Text hier", "mein_foto.jpg")`

### Seiten ohne Bilder

Du kannst auch Seiten ohne Bilder erstellen:
```python
mein_buch.add_page("Nur Text, kein Bild")
```

### Einzelne Seiten anzeigen

Statt das ganze Buch anzuzeigen, kannst du auch einzelne Seiten zeigen:
```python
# Zeige die erste Seite (Index beginnt bei 0)
mein_buch.display_page(0)

# Zeige die zweite Seite
mein_buch.display_page(1)
```

### Informationen abrufen

Du kannst auch Informationen über dein Buch abrufen:
```python
# Wie viele Seiten hat mein Buch?
anzahl_seiten = mein_buch.get_total_pages()
print(f"Mein Buch hat {anzahl_seiten} Seiten")

# Eine bestimmte Seite abrufen
seite = mein_buch.get_page(0)
print(seite["text"])  # Zeigt den Text der ersten Seite
```

## ✅ Testen ob alles funktioniert

Möchtest du überprüfen, ob alles korrekt installiert ist?

Führe die Tests aus:
```bash
python3 test_book_builder.py
```

Wenn alles funktioniert, siehst du:
```
✓ ALLE TESTS BESTANDEN!
```

## 📖 Vollständiges Beispiel für Einsteiger

Hier ist ein komplettes Beispiel, das du kopieren und anpassen kannst:

```python
from book_builder import InteractiveBook

# Schritt 1: Erstelle ein Buch
mein_buch = InteractiveBook("Die Reise zum Mond")

# Schritt 2: Füge Seiten mit Geschichten hinzu
mein_buch.add_page(
    "Max war ein kleiner Junge mit großen Träumen. "
    "Er wollte schon immer zum Mond fliegen!"
)

mein_buch.add_page(
    "Eines Tages baute er eine Rakete aus Kartons "
    "und Alufolie. Sie glänzte in der Sonne!"
)

mein_buch.add_page(
    "Mit einem lauten 'ZOOM!' startete die Rakete. "
    "Max war auf dem Weg zum Mond!"
)

mein_buch.add_page(
    "Als er auf dem Mond landete, machte er einen "
    "riesigen Sprung. Alles war so leicht hier!"
)

mein_buch.add_page(
    "Nach einem aufregenden Tag kehrte Max zurück. "
    "Aber das war erst der Anfang seiner Abenteuer!"
)

# Schritt 3: Zeige das Buch an
print("\n🌟 Dein Buch wird jetzt angezeigt: 🌟\n")
mein_buch.display_all()

# Bonustipp: Zeige wie viele Seiten dein Buch hat
print(f"\n📊 Dein Buch hat {mein_buch.get_total_pages()} Seiten!")
```

## 🆘 Häufige Probleme und Lösungen

### Problem: "python3 ist nicht erkannt"
**Lösung:** 
- Versuche `python` statt `python3`
- Stelle sicher, dass Python installiert ist
- Überprüfe, ob Python zum PATH hinzugefügt wurde

### Problem: "ModuleNotFoundError: No module named 'book_builder'"
**Lösung:**
- Stelle sicher, dass du im richtigen Ordner bist
- Die Datei `book_builder.py` muss im gleichen Ordner sein
- Navigiere mit `cd` zum richtigen Ordner

### Problem: Keine Ausgabe / Schwarzer Bildschirm
**Lösung:**
- Überprüfe, ob dein Code `display_all()` oder `display_page()` aufruft
- Stelle sicher, dass du Seiten zum Buch hinzugefügt hast

### Problem: Bilder werden nicht angezeigt
**Lösung:**
- Das Programm zeigt aktuell nur Bildpfade an, nicht die Bilder selbst
- Du siehst z.B. `[Bild: mein_foto.jpg]` - das ist normal!
- Die Bilder werden in einer späteren Version vielleicht richtig angezeigt

## 🎓 Nächste Schritte

Jetzt, wo du die Grundlagen kennst:

1. **Experimentiere!** Ändere den Code und schau, was passiert
2. **Erstelle dein eigenes Buch** über ein Thema, das dich interessiert
3. **Teile deine Kreationen** mit Freunden und Familie
4. **Lerne mehr Python** - Es gibt viele kostenlose Tutorials online

## 📚 Weitere Ressourcen

- **README.md** - Technische Dokumentation
- **Python Tutorial** - https://docs.python.org/de/3/tutorial/
- **GitHub Repository** - https://github.com/deranderechris/interaktive_ki_book_builder

## ❓ Fragen?

Wenn du Fragen hast oder Hilfe brauchst:
1. Lies nochmal diese Anleitung durch
2. Führe die Tests aus, um zu sehen, ob alles funktioniert
3. Schaue dir die Beispiele an
4. Öffne ein Issue auf GitHub

---

**Viel Spaß beim Erstellen deiner eigenen interaktiven Bücher!** 📚✨

*Tipp: Speichere diese Anleitung als Favorit, damit du sie immer griffbereit hast!*
