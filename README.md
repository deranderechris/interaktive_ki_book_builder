# interaktive_ki_book_builder
hiermit kann jeder sein eigenes interaktives Buch mit Bildern erstellen

## Installation

No external dependencies are required. The application uses only Python standard library.

```bash
# Optional: Install from requirements.txt (currently empty)
pip install -r requirements.txt
```

## Usage

### Run with an example book

```bash
python src/main.py --example dein_gespieltbuch.json
```

Or with the full path:

```bash
python src/main.py --example examples/dein_gespieltbuch.json
```

### Show help

```bash
python src/main.py --help
```

## Example Files

The repository includes example book configurations in the `examples/` directory:

- `dein_gespieltbuch.json` - A sample interactive book in German

## Book JSON Format

Books are defined using JSON files with the following structure:

```json
{
  "title": "Your Book Title",
  "author": "Author Name",
  "description": "Book description",
  "chapters": [
    {
      "title": "Chapter Title",
      "content": "Chapter content text...",
      "image": "path/to/image.jpg",
      "choices": [
        {
          "text": "Choice text",
          "next_chapter": 2
        }
      ]
    }
  ]
}
```

## Features

- Load interactive books from JSON configuration files
- Support for chapters with titles, content, and images
- Interactive choice-based navigation (planned)
- Simple command-line interface
