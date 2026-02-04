#!/usr/bin/env python3
"""
Interactive Book Builder - Main Entry Point
Allows creating and running interactive gamebooks with images.
"""

import argparse
import json
import sys
from pathlib import Path


def load_gamebook(filepath):
    """Load a gamebook from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filepath}': {e}")
        sys.exit(1)


def display_scene(scene):
    """Display a scene from the gamebook."""
    print("\n" + "=" * 60)
    print(f"\n{scene.get('title', 'Untitled Scene')}")
    print("-" * 60)
    print(f"\n{scene.get('text', '')}\n")
    
    if 'image' in scene:
        print(f"[Image: {scene['image']}]")
    
    choices = scene.get('choices', [])
    if choices:
        print("\nChoices:")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice.get('text', 'Continue')}")
    else:
        print("\n[End of story]")
    
    print("=" * 60)


def run_gamebook(gamebook_data):
    """Run an interactive gamebook."""
    print("\n" + "=" * 60)
    print(f"  {gamebook_data.get('title', 'Interactive Gamebook')}")
    print("=" * 60)
    
    if 'description' in gamebook_data:
        print(f"\n{gamebook_data['description']}\n")
    
    scenes = gamebook_data.get('scenes', [])
    if not scenes:
        print("Error: No scenes found in gamebook.")
        return
    
    current_scene_id = gamebook_data.get('start_scene', scenes[0].get('id', 0))
    
    while True:
        # Find current scene
        current_scene = None
        for scene in scenes:
            if scene.get('id') == current_scene_id:
                current_scene = scene
                break
        
        if not current_scene:
            print(f"\nError: Scene '{current_scene_id}' not found.")
            break
        
        # Display the scene
        display_scene(current_scene)
        
        # Get choices
        choices = current_scene.get('choices', [])
        if not choices:
            # End of story
            break
        
        # Get user input
        while True:
            try:
                choice_input = input("\nEnter your choice (number or 'q' to quit): ").strip()
                
                if choice_input.lower() == 'q':
                    print("\nThanks for playing!")
                    return
                
                choice_num = int(choice_input)
                if 1 <= choice_num <= len(choices):
                    selected_choice = choices[choice_num - 1]
                    current_scene_id = selected_choice.get('next_scene')
                    if current_scene_id is None:
                        print("\nEnd of story. Thanks for playing!")
                        return
                    break
                else:
                    print(f"Please enter a number between 1 and {len(choices)}.")
            except ValueError:
                print("Please enter a valid number or 'q' to quit.")
            except KeyboardInterrupt:
                print("\n\nThanks for playing!")
                return


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description='Interactive Book Builder - Create and play interactive gamebooks'
    )
    parser.add_argument(
        '--example',
        type=str,
        help='Path to an example gamebook JSON file to load and play'
    )
    
    args = parser.parse_args()
    
    if args.example:
        # Load and run the example gamebook
        example_path = Path(args.example)
        print(f"Loading example from: {example_path}")
        gamebook_data = load_gamebook(example_path)
        run_gamebook(gamebook_data)
    else:
        # No arguments provided, show help
        parser.print_help()
        print("\nExample usage:")
        print("  python src/main.py --example examples/mini_gamebook.json")


if __name__ == '__main__':
    main()
