"""
Tests für den Interaktiven KI Book Builder
"""

import sys
from book_builder import InteractiveBook, create_example_book


def test_create_book():
    """Test: Erstelle ein neues Buch"""
    book = InteractiveBook("Testbuch")
    assert book.title == "Testbuch"
    assert book.get_total_pages() == 0
    print("✓ test_create_book bestanden")


def test_add_page():
    """Test: Füge eine Seite hinzu"""
    book = InteractiveBook()
    page_id = book.add_page("Dies ist eine Testseite", "test.jpg")
    assert page_id == 0
    assert book.get_total_pages() == 1
    print("✓ test_add_page bestanden")


def test_get_page():
    """Test: Rufe eine Seite ab"""
    book = InteractiveBook()
    book.add_page("Seite 1", "bild1.jpg")
    page = book.get_page(0)
    assert page is not None
    assert page["text"] == "Seite 1"
    assert page["image"] == "bild1.jpg"
    print("✓ test_get_page bestanden")


def test_multiple_pages():
    """Test: Füge mehrere Seiten hinzu"""
    book = InteractiveBook()
    book.add_page("Seite 1")
    book.add_page("Seite 2")
    book.add_page("Seite 3")
    assert book.get_total_pages() == 3
    print("✓ test_multiple_pages bestanden")


def test_display_page():
    """Test: Zeige eine Seite an"""
    book = InteractiveBook("Anzeigetest")
    book.add_page("Testinhalt", "test.jpg")
    result = book.display_page(0)
    assert result == True
    print("✓ test_display_page bestanden")


def test_example_book():
    """Test: Erstelle ein Beispielbuch"""
    book = create_example_book()
    assert book.get_total_pages() > 0
    assert book.title == "Mein erstes interaktives Buch"
    print("✓ test_example_book bestanden")


def run_all_tests():
    """Führe alle Tests aus"""
    print("\n" + "=" * 50)
    print("Starte Tests für den Interaktiven KI Book Builder")
    print("=" * 50 + "\n")
    
    tests = [
        test_create_book,
        test_add_page,
        test_get_page,
        test_multiple_pages,
        test_display_page,
        test_example_book
    ]
    
    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} fehlgeschlagen: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} Fehler: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    if failed == 0:
        print("✓ ALLE TESTS BESTANDEN!")
        print("=" * 50 + "\n")
        return 0
    else:
        print(f"✗ {failed} Test(s) fehlgeschlagen")
        print("=" * 50 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
