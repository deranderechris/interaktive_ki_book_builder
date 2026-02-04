"""
Utility-Funktionen für den Interactive KI Book Builder
"""

import logging
import json
from pathlib import Path
from typing import Dict, Any
import os


def setup_logging(verbose: bool = False) -> logging.Logger:
    """
    Richtet das Logging-System ein
    
    Args:
        verbose: Wenn True, wird Debug-Level verwendet
    
    Returns:
        Logger-Instanz
    """
    log_level = logging.DEBUG if verbose else logging.INFO
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logger = logging.getLogger('interactive_ki_book')
    return logger


def load_config(config_path: str = '.env') -> Dict[str, Any]:
    """
    Lädt die Konfiguration aus einer Datei
    
    Args:
        config_path: Pfad zur Konfigurationsdatei
    
    Returns:
        Dictionary mit Konfigurationswerten
    """
    config = {}
    
    # Versuche .env zu laden
    env_path = Path(config_path)
    if env_path.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_path)
        except ImportError:
            pass
    
    # Versuche config.json zu laden
    config_json = Path('config.json')
    if config_json.exists():
        with open(config_json, 'r', encoding='utf-8') as f:
            config = json.load(f)
    
    # Umgebungsvariablen haben Vorrang
    if os.getenv('OPENAI_API_KEY'):
        config['openai_api_key'] = os.getenv('OPENAI_API_KEY')
    
    return config


def validate_json_file(file_path: str) -> bool:
    """
    Validiert, ob eine Datei gültiges JSON enthält
    
    Args:
        file_path: Pfad zur JSON-Datei
    
    Returns:
        True wenn die Datei gültiges JSON enthält, sonst False
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, FileNotFoundError):
        return False


def create_example_story(output_path: str = 'example_story.json') -> str:
    """
    Erstellt eine Beispiel-Geschichtendatei
    
    Args:
        output_path: Pfad für die Ausgabedatei
    
    Returns:
        Pfad zur erstellten Datei
    """
    example_story = {
        "title": "Das magische Abenteuer",
        "author": "KI Book Builder",
        "pages": [
            {
                "id": "start",
                "text": "Du stehst vor einem dunklen Wald. Ein schmaler Pfad führt hinein.",
                "image_prompt": "Ein dunkler, mystischer Wald mit einem schmalen Pfad",
                "choices": [
                    {
                        "text": "Den Wald betreten",
                        "next": "forest"
                    },
                    {
                        "text": "Umkehren",
                        "next": "home"
                    }
                ]
            },
            {
                "id": "forest",
                "text": "Im Wald entdeckst du eine Lichtung mit einem leuchtenden Kristall.",
                "image_prompt": "Eine Waldlichtung mit einem magischen leuchtenden Kristall",
                "choices": [
                    {
                        "text": "Den Kristall berühren",
                        "next": "magic"
                    },
                    {
                        "text": "Zurück zum Waldrand",
                        "next": "start"
                    }
                ]
            },
            {
                "id": "magic",
                "text": "Der Kristall beginnt zu leuchten und erfüllt dich mit magischer Energie. Du hast gewonnen!",
                "image_prompt": "Ein leuchtender magischer Kristall mit Energiestrahlen"
            },
            {
                "id": "home",
                "text": "Du kehrst sicher nach Hause zurück. Das Abenteuer endet hier.",
                "image_prompt": "Ein gemütliches Haus bei Sonnenuntergang"
            }
        ]
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(example_story, f, ensure_ascii=False, indent=2)
    
    return output_path
