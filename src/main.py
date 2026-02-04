#!/usr/bin/env python3
"""
Interactive Book Builder
Create your own interactive book with images
"""

import argparse
import json
import sys
from pathlib import Path


def load_book_config(filepath):
    """Load book configuration from JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filepath}': {e}")
        sys.exit(1)


def create_book(config):
    """Create an interactive book from configuration"""
    print("=" * 60)
    print("Interactive Book Builder")
    print("=" * 60)
    print()
    
    # Display book title
    if 'title' in config:
        print(f"Title: {config['title']}")
    
    # Display book author
    if 'author' in config:
        print(f"Author: {config['author']}")
    
    # Display book description
    if 'description' in config:
        print(f"Description: {config['description']}")
    
    print()
    print("-" * 60)
    
    # Process chapters/pages
    if 'chapters' in config:
        print(f"\nChapters: {len(config['chapters'])}")
        for i, chapter in enumerate(config['chapters'], 1):
            print(f"\nChapter {i}: {chapter.get('title', 'Untitled')}")
            if 'content' in chapter:
                print(f"  Content: {chapter['content'][:100]}..." if len(chapter.get('content', '')) > 100 else f"  Content: {chapter.get('content', '')}")
            if 'image' in chapter:
                print(f"  Image: {chapter['image']}")
    
    print()
    print("=" * 60)
    print("Book loaded successfully!")
    print("=" * 60)


def main():
    """Main entry point for the interactive book builder"""
    parser = argparse.ArgumentParser(
        description='Interactive Book Builder - Create your own interactive book with images',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--example',
        type=str,
        metavar='FILE',
        help='Load an example book configuration from a JSON file'
    )
    
    args = parser.parse_args()
    
    if args.example:
        # Handle relative paths from examples directory
        example_file = Path(args.example)
        
        # If the file doesn't exist as-is, try looking in examples directory
        if not example_file.exists():
            examples_dir = Path(__file__).parent.parent / 'examples'
            example_file = examples_dir / args.example
        
        # Load and create the book
        config = load_book_config(example_file)
        create_book(config)
    else:
        # No arguments provided, show help
        parser.print_help()


if __name__ == '__main__':
    main()
