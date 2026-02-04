"""
Interaktive KI Book Builder
Ein einfaches Tool zum Erstellen interaktiver Bücher mit Bildern
"""

class InteractiveBook:
    """Klasse zur Verwaltung eines interaktiven Buches"""
    
    def __init__(self, title="Mein Buch"):
        self.title = title
        self.pages = []
    
    def add_page(self, text, image_path=None):
        """Fügt eine neue Seite zum Buch hinzu"""
        page = {
            "text": text,
            "image": image_path
        }
        self.pages.append(page)
        return len(self.pages) - 1
    
    def get_page(self, page_number):
        """Gibt eine bestimmte Seite zurück"""
        if 0 <= page_number < len(self.pages):
            return self.pages[page_number]
        return None
    
    def get_total_pages(self):
        """Gibt die Gesamtzahl der Seiten zurück"""
        return len(self.pages)
    
    def display_page(self, page_number):
        """Zeigt eine Seite an"""
        page = self.get_page(page_number)
        if page:
            print(f"\n=== Seite {page_number + 1} von {self.get_total_pages()} ===")
            print(f"Titel: {self.title}")
            print(f"\n{page['text']}")
            if page.get('image'):
                print(f"[Bild: {page.get('image')}]")
            print("=" * 50)
            return True
        return False
    
    def display_all(self):
        """Zeigt alle Seiten des Buches an"""
        print(f"\n{'=' * 50}")
        print(f"BUCH: {self.title}")
        print(f"{'=' * 50}")
        for i in range(self.get_total_pages()):
            self.display_page(i)
        print(f"{'=' * 50}\n")


def create_example_book():
    """Erstellt ein Beispielbuch"""
    book = InteractiveBook("Mein erstes interaktives Buch")
    
    book.add_page(
        "Es war einmal ein kleiner Frosch, der in einem wunderschönen Teich lebte.",
        "frosch.jpg"
    )
    
    book.add_page(
        "Der Frosch liebte es, auf Seerosenblättern zu sitzen und die Sonne zu genießen.",
        "seerose.jpg"
    )
    
    book.add_page(
        "Eines Tages machte er sich auf eine große Abenteuerreise.",
        "abenteuer.jpg"
    )
    
    return book


if __name__ == "__main__":
    # Erstelle ein Beispielbuch
    book = create_example_book()
    
    # Zeige alle Seiten an
    book.display_all()
    
    print("✓ Interaktives Buch erfolgreich erstellt!")
