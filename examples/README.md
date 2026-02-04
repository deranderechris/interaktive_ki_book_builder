# Beispiele - Interaktiver KI Book Builder

Dieses Verzeichnis enthält Beispielgeschichten für den Interaktiven KI Book Builder.

## beispiel_buch.json

**Das Abenteuer im Verzauberten Wald**

Eine vollständige Fantasy-Geschichte mit:
- 12 verschiedenen Abschnitten
- 3 unterschiedliche Startoptionen
- 9 verschiedene Enden
- Vollständig generierte Bild-Prompts
- Magische Atmosphäre mit Feen, Eremiten und sprechenden Bäumen

### Story-Struktur

```
Start
├── Waldpfad
│   ├── Feenkreis (Ende)
│   ├── Steinhütte (Ende)
│   └── Flüstern lauschen (Ende)
├── Verlassenes Dorf
│   ├── Brunnen (Ende)
│   ├── Kapelle (Ende)
│   └── Haus (Ende)
└── Warten & Beobachten
    ├── Lichtern folgen (Ende)
    └── Gesang folgen (Ende)
```

### Spielen

```bash
python main.py examples/beispiel_buch.json
```

### Features

- **Verzweigte Handlung**: Jede Entscheidung führt zu einem anderen Pfad
- **Atmosphärische Beschreibungen**: Jede Szene ist detailliert beschrieben
- **Automatische Bild-Prompts**: Jeder Abschnitt hat einen kopierbaren KI-Bildprompt
- **Multiple Enden**: 9 verschiedene Möglichkeiten, die Geschichte zu beenden

## Eigene Beispiele hinzufügen

Du kannst deine eigenen Beispielgeschichten zu diesem Verzeichnis hinzufügen:

1. Erstelle eine neue JSON-Datei mit deiner Geschichte
2. Speichere sie in diesem Verzeichnis
3. Teile sie mit anderen!

## Tipps für gute Geschichten

1. **Klare Struktur**: Plane deine Geschichte mit einem Diagramm
2. **Interessante Entscheidungen**: Jede Wahl sollte bedeutsam sein
3. **Verschiedene Enden**: Mindestens 3-5 unterschiedliche Ausgänge
4. **Atmosphäre**: Nutze beschreibende Sprache für bessere Bild-Prompts
5. **Balance**: Nicht zu kurz, nicht zu lang (8-15 Abschnitte sind ideal)

## Bild-Prompt Qualität

Die Beispielgeschichte nutzt Schlüsselwörter, die der Prompt-Generator erkennt:
- Wald, Bäume → `forest setting`
- Dunkel, Nacht → `dark atmosphere`
- Magie, Feen → `magical atmosphere`
- Frieden, Ruhe → `peaceful atmosphere`

Verwende solche Wörter in deinen Geschichten für bessere Prompts!
