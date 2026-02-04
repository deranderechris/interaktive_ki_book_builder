import json
import os


class StoryManager:
    """Manages an interactive story/gamebook with choices and navigation."""
    
    def __init__(self, story_file):
        """Initialize the StoryManager with a JSON story file.
        
        Args:
            story_file: Path to the JSON file containing the story structure
        """
        self.story_file = story_file
        self.story_data = self._load_story()
        self.current_node = self.story_data.get("start", "start")
    
    def _load_story(self):
        """Load and parse the story JSON file.
        
        Returns:
            dict: The parsed story data
            
        Raises:
            FileNotFoundError: If the story file doesn't exist
            json.JSONDecodeError: If the file is not valid JSON
        """
        if not os.path.exists(self.story_file):
            raise FileNotFoundError(f"Story file not found: {self.story_file}")
        
        with open(self.story_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _display_node(self, node_id):
        """Display the content of a story node.
        
        Args:
            node_id: The ID of the node to display
            
        Returns:
            dict: The node data or None if not found
        """
        nodes = self.story_data.get("nodes", {})
        if node_id not in nodes:
            print(f"Fehler: Knoten '{node_id}' wurde nicht gefunden.")
            return None
        
        node = nodes[node_id]
        print("\n" + "=" * 60)
        print(node.get("text", ""))
        print("=" * 60)
        
        # Display image info if available
        if "image" in node:
            print(f"[Bild: {node['image']}]")
        
        return node
    
    def _get_user_choice(self, choices):
        """Get a valid choice from the user.
        
        Args:
            choices: List of choice dictionaries with 'text' and 'next' keys
            
        Returns:
            str: The next node ID based on user's choice
        """
        print("\nWas möchtest du tun?")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice.get('text', 'Unbekannte Option')}")
        
        while True:
            try:
                user_input = input("\nDeine Wahl (Nummer): ")
                choice_num = int(user_input)
                if 1 <= choice_num <= len(choices):
                    return choices[choice_num - 1].get("next")
                else:
                    print(f"Bitte wähle eine Nummer zwischen 1 und {len(choices)}.")
            except ValueError:
                print("Bitte gib eine gültige Nummer ein.")
            except (KeyboardInterrupt, EOFError):
                print("\n\nSpiel beendet.")
                return None
    
    def play(self):
        """Start and manage the interactive story gameplay loop."""
        print("\n--- Story beginnt ---\n")
        
        while True:
            node = self._display_node(self.current_node)
            
            if node is None:
                print("Das Spiel kann nicht fortgesetzt werden.")
                break
            
            # Check if this is an end node
            if node.get("end", False):
                print("\n--- ENDE ---")
                print(node.get("ending_message", "Danke fürs Spielen!"))
                break
            
            # Get choices
            choices = node.get("choices", [])
            if not choices:
                print("\nKeine weiteren Optionen verfügbar. Story endet hier.")
                break
            
            # Get user's choice
            next_node = self._get_user_choice(choices)
            if next_node is None:
                break
            
            self.current_node = next_node
