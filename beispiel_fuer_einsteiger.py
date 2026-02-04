"""
Einfaches Beispiel für Einsteiger
==================================

Dies ist ein einfaches Beispiel, das du als Vorlage für dein eigenes Buch
verwenden kannst. Ändere einfach die Texte und erstelle deine eigene Geschichte!

"""

from book_builder import InteractiveBook

# Erstelle ein neues Buch mit einem Titel
mein_buch = InteractiveBook("Meine erste Geschichte")

# Füge Seiten hinzu - ändere den Text nach Belieben!
mein_buch.add_page(
    "Es war einmal an einem sonnigen Tag im Frühling...",
    "bild1.jpg"  # Optional: Ersetze dies durch deinen Bildpfad
)

mein_buch.add_page(
    "Die Sonne schien hell und die Vögel sangen fröhliche Lieder.",
    "bild2.jpg"
)

mein_buch.add_page(
    "Plötzlich begann ein spannendes Abenteuer!",
    "bild3.jpg"
)

mein_buch.add_page(
    "Nach vielen aufregenden Erlebnissen kehrte alles zur Ruhe zurück."
)

mein_buch.add_page(
    "Und wenn sie nicht gestorben sind, dann leben sie noch heute. Ende.",
    "bild5.jpg"
)

# Zeige das gesamte Buch an
print("\n" + "="*60)
print("DEIN BUCH WIRD JETZT ANGEZEIGT")
print("="*60 + "\n")

mein_buch.display_all()

# Zeige zusätzliche Informationen
print(f"\n✨ Dein Buch hat {mein_buch.get_total_pages()} Seiten!")
print("✨ Ändere dieses Beispiel, um deine eigene Geschichte zu schreiben!")
