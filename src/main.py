from story_manager import StoryManager

def main():
    print("Willkommen zum Interactive KI Book Builder!")
    example_file = input("Gib den Pfad zu deinem Spielbuch ein (z.B. examples/mini_gamebook.json): ")
    story = StoryManager(example_file)
    story.play()

if __name__ == "__main__":
    main()
