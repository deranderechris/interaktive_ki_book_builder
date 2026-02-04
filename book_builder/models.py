"""
Modelle für das interaktive Buchsystem.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json


@dataclass
class Decision:
    """Repräsentiert eine Entscheidungsoption in einem Abschnitt."""
    option: str  # A, B, C, or D
    text: str
    next_section_id: str
    
    def to_dict(self) -> Dict:
        return {
            'option': self.option,
            'text': self.text,
            'next_section_id': self.next_section_id
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Decision':
        return cls(
            option=data['option'],
            text=data['text'],
            next_section_id=data['next_section_id']
        )


@dataclass
class Section:
    """Repräsentiert einen Abschnitt/eine Szene in der Geschichte."""
    id: str
    title: str
    text: str
    decisions: List[Decision] = field(default_factory=list)
    is_ending: bool = False
    image_prompt: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'decisions': [d.to_dict() for d in self.decisions],
            'is_ending': self.is_ending,
            'image_prompt': self.image_prompt
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Section':
        decisions = [Decision.from_dict(d) for d in data.get('decisions', [])]
        return cls(
            id=data['id'],
            title=data['title'],
            text=data['text'],
            decisions=decisions,
            is_ending=data.get('is_ending', False),
            image_prompt=data.get('image_prompt')
        )


@dataclass
class Memory:
    """Verwaltet das Gedächtnis des Spielers während der Geschichte."""
    visited_sections: List[str] = field(default_factory=list)
    decisions_made: List[Dict[str, str]] = field(default_factory=list)
    hints: List[str] = field(default_factory=list)
    open_paths: List[str] = field(default_factory=list)
    summary: str = ""
    
    def add_visit(self, section_id: str):
        """Fügt einen besuchten Abschnitt hinzu."""
        if section_id not in self.visited_sections:
            self.visited_sections.append(section_id)
    
    def add_decision(self, section_id: str, decision: str):
        """Speichert eine getroffene Entscheidung."""
        self.decisions_made.append({
            'section_id': section_id,
            'decision': decision,
            'order': len(self.decisions_made) + 1
        })
    
    def add_hint(self, hint: str):
        """Fügt einen Hinweis hinzu."""
        if hint not in self.hints:
            self.hints.append(hint)
    
    def add_open_path(self, path: str):
        """Fügt einen offenen Pfad hinzu."""
        if path not in self.open_paths:
            self.open_paths.append(path)
    
    def remove_open_path(self, path: str):
        """Entfernt einen abgeschlossenen Pfad."""
        if path in self.open_paths:
            self.open_paths.remove(path)
    
    def update_summary(self, text: str):
        """Aktualisiert die Zusammenfassung."""
        self.summary = text
    
    def to_dict(self) -> Dict:
        return {
            'visited_sections': self.visited_sections,
            'decisions_made': self.decisions_made,
            'hints': self.hints,
            'open_paths': self.open_paths,
            'summary': self.summary
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Memory':
        return cls(
            visited_sections=data.get('visited_sections', []),
            decisions_made=data.get('decisions_made', []),
            hints=data.get('hints', []),
            open_paths=data.get('open_paths', []),
            summary=data.get('summary', '')
        )


@dataclass
class Book:
    """Repräsentiert ein interaktives Buch."""
    title: str
    author: str
    description: str
    start_section_id: str
    sections: Dict[str, Section] = field(default_factory=dict)
    
    def add_section(self, section: Section):
        """Fügt einen Abschnitt zum Buch hinzu."""
        self.sections[section.id] = section
    
    def get_section(self, section_id: str) -> Optional[Section]:
        """Holt einen Abschnitt nach ID."""
        return self.sections.get(section_id)
    
    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'start_section_id': self.start_section_id,
            'sections': {sid: s.to_dict() for sid, s in self.sections.items()}
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        sections = {sid: Section.from_dict(s) for sid, s in data.get('sections', {}).items()}
        return cls(
            title=data['title'],
            author=data['author'],
            description=data['description'],
            start_section_id=data['start_section_id'],
            sections=sections
        )
