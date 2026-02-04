#!/usr/bin/env python3
"""
Interactive KI Book Builder - Main Entry Point
Erstelle dein eigenes interaktives Buch mit KI-generierten Bildern
"""

import argparse
import sys
from story_manager import StoryManager
from image_generator import ImageGenerator
from utils import setup_logging, load_config


def main():
    """Hauptfunktion für den Interactive KI Book Builder"""
    parser = argparse.ArgumentParser(
        description='Erstelle interaktive Bücher mit KI-generierten Bildern'
    )
    parser.add_argument(
        'input_file',
        help='Pfad zur JSON-Datei mit der Geschichte'
    )
    parser.add_argument(
        '--output',
        '-o',
        default='output',
        help='Ausgabeverzeichnis für das generierte Buch'
    )
    parser.add_argument(
        '--no-images',
        action='store_true',
        help='Bilder nicht generieren'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Ausführliche Ausgabe'
    )
    
    args = parser.parse_args()
    
    # Logging einrichten
    logger = setup_logging(verbose=args.verbose)
    logger.info("Interactive KI Book Builder gestartet")
    
    try:
        # Konfiguration laden
        config = load_config()
        
        # Story Manager initialisieren
        story_manager = StoryManager(args.input_file)
        story_data = story_manager.load_story()
        
        logger.info(f"Geschichte geladen: {story_data.get('title', 'Unbekannt')}")
        
        # Bild-Generator initialisieren (falls gewünscht)
        if not args.no_images:
            image_gen = ImageGenerator(config)
            logger.info("Generiere Bilder für die Geschichte...")
            images = image_gen.generate_images(story_data)
            logger.info(f"{len(images)} Bilder erfolgreich generiert")
        
        # Buch erstellen
        output_path = story_manager.create_book(
            story_data,
            args.output,
            include_images=not args.no_images
        )
        
        logger.info(f"Buch erfolgreich erstellt: {output_path}")
        
    except FileNotFoundError as e:
        logger.error(f"Datei nicht gefunden: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Fehler bei der Bucherstellung: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
