# interaktive_ki_book_builder

hiermit kann jeder sein eigenes interaktives Buch mit Bildern erstellen

## 📖 Für Einsteiger

**Neu hier? Starte mit unserer [Schritt-für-Schritt Anleitung für Einsteiger](ERSTE_SCHRITTE.md)!**

Die einsteigerfreundliche Anleitung erklärt alles von Anfang an - perfekt wenn du gerade erst mit dem Programmieren beginnst!

## Funktionen

- Erstellen von interaktiven Büchern mit Text und Bildern
- Einfache API zum Hinzufügen von Seiten
- Anzeigen einzelner Seiten oder des gesamten Buches
- Python-basierte Implementierung ohne externe Abhängigkeiten

## Installation

Keine externen Abhängigkeiten erforderlich. Python 3.x wird benötigt.

```bash
# Optional: Installiere zukünftige Abhängigkeiten
pip install -r requirements.txt
```

## Verwendung

### Beispiel ausführen

```bash
python3 book_builder.py
```

### Eigenes Buch erstellen

```python
from book_builder import InteractiveBook

# Erstelle ein neues Buch
book = InteractiveBook("Mein Buchtitel")

# Füge Seiten hinzu
book.add_page("Dies ist die erste Seite", "bild1.jpg")
book.add_page("Dies ist die zweite Seite", "bild2.jpg")

# Zeige das Buch an
book.display_all()
```

## Tests ausführen

```bash
python3 test_book_builder.py
```

Alle Tests sollten erfolgreich durchlaufen:
```
✓ ALLE TESTS BESTANDEN!
```

## Status

✓ Grundfunktionalität implementiert und getestet
✓ Alle Tests bestehen
✓ Beispielbuch funktioniert
