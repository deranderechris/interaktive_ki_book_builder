#!/usr/bin/env python3
"""
Beispiel für die Nutzung des Interaktiven Book Builders
"""

from book_builder import InteractivBook


def create_example_book():
    """Erstellt ein Beispielbuch"""
    
    # Neues Buch erstellen
    book = InteractivBook(
        title="Eine Reise durch die Zeit",
        author="Max Mustermann"
    )
    
    # Kapitel hinzufügen
    book.add_chapter(
        chapter_title="Der Anfang",
        content="Es war einmal in einer kleinen Stadt, wo unsere Geschichte beginnt. "
                "Die Sonne schien hell und die Vögel sangen ihre Lieder.",
        image_path="images/beginning.jpg"
    )
    
    book.add_chapter(
        chapter_title="Die Entdeckung",
        content="Eines Tages fand ich eine alte Karte auf dem Dachboden. "
                "Sie zeigte geheimnisvolle Orte, die ich noch nie gesehen hatte.",
        image_path="images/discovery.jpg"
    )
    
    book.add_chapter(
        chapter_title="Das Abenteuer",
        content="Ich machte mich auf den Weg, um diese Orte zu erkunden. "
                "Was ich dort fand, übertraf alle meine Erwartungen.",
        image_path="images/adventure.jpg"
    )
    
    book.add_chapter(
        chapter_title="Die Rückkehr",
        content="Nach vielen Abenteuern kehrte ich nach Hause zurück, "
                "voller neuer Erfahrungen und Geschichten zu erzählen.",
        image_path="images/return.jpg"
    )
    
    # Buch-Informationen anzeigen
    book.display_info()
    
    # Buch in verschiedenen Formaten speichern
    book.save_to_json("zeitreise_buch.json")
    book.save_to_html("zeitreise_buch.html")
    
    print("\n✓ Beispielbuch wurde erfolgreich erstellt!")
    print("  - zeitreise_buch.json")
    print("  - zeitreise_buch.html")


if __name__ == "__main__":
    create_example_book()
