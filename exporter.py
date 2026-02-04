"""
Export-Funktionalität für Interactive Stories
"""
from models import Story, Section
from typing import Optional
import os


class StoryExporter:
    """Exportiert Stories in verschiedene Formate"""
    
    def __init__(self, story: Story):
        self.story = story
    
    def export_to_html(self, filename: str, interactive: bool = True):
        """
        Exportiert die Story als HTML-Datei
        
        Args:
            filename: Zieldatei
            interactive: True für interaktives Buch, False für druckbares Buch
        """
        if interactive:
            html_content = self._generate_interactive_html()
        else:
            html_content = self._generate_printable_html()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def _generate_interactive_html(self) -> str:
        """Generiert interaktives HTML mit JavaScript"""
        html_template = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Georgia', serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5dc;
            color: #333;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        h1 {{
            color: #654321;
            font-size: 2.5em;
        }}
        .description {{
            font-style: italic;
            color: #666;
        }}
        .section {{
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        .section-title {{
            color: #654321;
            font-size: 1.8em;
            margin-bottom: 15px;
        }}
        .section-content {{
            line-height: 1.8;
            margin-bottom: 20px;
        }}
        .image-prompt {{
            background-color: #fff8dc;
            padding: 10px;
            border-left: 4px solid #daa520;
            margin: 15px 0;
            font-size: 0.9em;
            font-style: italic;
        }}
        .choices {{
            margin-top: 30px;
        }}
        .choice {{
            background-color: #8b7355;
            color: white;
            padding: 15px 20px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            width: 100%;
            text-align: left;
            transition: background-color 0.3s;
        }}
        .choice:hover {{
            background-color: #654321;
        }}
        .choice-label {{
            font-weight: bold;
            margin-right: 10px;
        }}
        .hints {{
            background-color: #fffacd;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
        }}
        .ending {{
            text-align: center;
            font-size: 1.2em;
            color: #654321;
            margin-top: 30px;
            padding: 20px;
            background-color: #fff8dc;
            border-radius: 10px;
        }}
        .restart {{
            background-color: #daa520;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            margin-top: 20px;
        }}
        .restart:hover {{
            background-color: #b8860b;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p class="description">{description}</p>
        {author_html}
    </div>
    <div id="story-container"></div>
    
    <script>
        const storyData = {story_json};
        let currentSectionId = storyData.start_section_id;
        
        function escapeHtml(text) {{
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }}
        
        function displaySection(sectionId) {{
            const section = storyData.sections[sectionId];
            if (!section) {{
                console.error("Section not found:", sectionId);
                return;
            }}
            
            let html = '<div class="section">';
            html += '<h2 class="section-title">' + escapeHtml(section.title) + '</h2>';
            html += '<div class="section-content">' + escapeHtml(section.content).replace(/\\n/g, '<br>') + '</div>';
            
            if (section.image_prompt) {{
                html += '<div class="image-prompt">🎨 Bild-Prompt: ' + escapeHtml(section.image_prompt) + '</div>';
            }}
            
            if (section.hints && section.hints.length > 0) {{
                html += '<div class="hints"><strong>💡 Hinweise:</strong><ul>';
                section.hints.forEach(hint => {{
                    html += '<li>' + escapeHtml(hint) + '</li>';
                }});
                html += '</ul></div>';
            }}
            
            if (section.choices && section.choices.length > 0) {{
                html += '<div class="choices">';
                section.choices.forEach(choice => {{
                    const label = choice.label ? '<span class="choice-label">' + escapeHtml(choice.label) + ')</span>' : '';
                    html += '<button class="choice" onclick="makeChoice(&apos;' + choice.next_section_id + '&apos;)">';
                    html += label + escapeHtml(choice.text);
                    html += '</button>';
                }});
                html += '</div>';
            }} else {{
                html += '<div class="ending">📖 Ende dieser Geschichte 📖</div>';
                html += '<button class="restart" onclick="restart()">Geschichte neu starten</button>';
            }}
            
            html += '</div>';
            
            document.getElementById('story-container').innerHTML = html;
            window.scrollTo(0, 0);
        }}
        
        function makeChoice(nextSectionId) {{
            currentSectionId = nextSectionId;
            displaySection(nextSectionId);
        }}
        
        function restart() {{
            currentSectionId = storyData.start_section_id;
            displaySection(currentSectionId);
        }}
        
        // Start the story
        displaySection(currentSectionId);
    </script>
</body>
</html>"""
        
        import json
        author_html = f'<p><em>von {self.story.author}</em></p>' if self.story.author else ''
        
        return html_template.format(
            title=self.story.title,
            description=self.story.description,
            author_html=author_html,
            story_json=json.dumps(self.story.to_dict(), ensure_ascii=False)
        )
    
    def _generate_printable_html(self) -> str:
        """Generiert druckbares HTML (alle Sections auf einmal)"""
        html_parts = ["""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{title} - Spielbuch</title>
    <style>
        body {{
            font-family: 'Georgia', serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        .cover {{
            page-break-after: always;
            text-align: center;
            padding: 100px 20px;
        }}
        h1 {{
            font-size: 3em;
            color: #654321;
        }}
        .section {{
            page-break-inside: avoid;
            margin-bottom: 40px;
            padding: 20px;
            border: 2px solid #654321;
            border-radius: 10px;
        }}
        .section-id {{
            background-color: #654321;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 10px;
        }}
        .section-title {{
            color: #654321;
            font-size: 1.5em;
        }}
        .choices {{
            margin-top: 20px;
            padding: 15px;
            background-color: #f5f5dc;
            border-radius: 5px;
        }}
        .choice {{
            margin: 10px 0;
            padding: 10px;
            background-color: white;
            border-left: 4px solid #8b7355;
        }}
        @media print {{
            .section {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    <div class="cover">
        <h1>{title}</h1>
        <p style="font-size: 1.5em;">{description}</p>
        {author_html}
        <p style="margin-top: 50px;">Starte bei Abschnitt: <strong>{start_section}</strong></p>
    </div>
""".format(
            title=self.story.title,
            description=self.story.description,
            author_html=f'<p><em>von {self.story.author}</em></p>' if self.story.author else '',
            start_section=self.story.start_section_id
        )]
        
        # Sortiere Sections nach ID
        sorted_sections = sorted(self.story.sections.items(), key=lambda x: x[0])
        
        for section_id, section in sorted_sections:
            html_parts.append(f"""
    <div class="section">
        <div class="section-id">{section_id}</div>
        <h2 class="section-title">{section.title}</h2>
        <div class="section-content">{section.content.replace(chr(10), '<br>')}</div>
""")
            
            if section.image_prompt:
                html_parts.append(f"""
        <div style="margin: 15px 0; padding: 10px; background-color: #fff8dc; border-left: 4px solid #daa520;">
            🎨 <em>Bild-Prompt: {section.image_prompt}</em>
        </div>
""")
            
            if section.hints:
                html_parts.append('        <div style="margin-top: 15px;"><strong>💡 Hinweise:</strong><ul>')
                for hint in section.hints:
                    html_parts.append(f'            <li>{hint}</li>')
                html_parts.append('        </ul></div>')
            
            if section.choices:
                html_parts.append('        <div class="choices"><strong>Wähle:</strong>')
                for choice in section.choices:
                    label = f'{choice.label}) ' if choice.label else '→ '
                    html_parts.append(f"""
            <div class="choice">{label}{choice.text} <em>(weiter zu {choice.next_section_id})</em></div>
""")
                html_parts.append('        </div>')
            else:
                html_parts.append('        <div style="text-align: center; margin-top: 20px; font-size: 1.2em;">📖 <strong>ENDE</strong> 📖</div>')
            
            html_parts.append('    </div>')
        
        html_parts.append("""
</body>
</html>""")
        
        return ''.join(html_parts)
    
    def export_to_markdown(self, filename: str):
        """Exportiert die Story als Markdown-Datei"""
        md_parts = [f"# {self.story.title}\n\n"]
        
        if self.story.description:
            md_parts.append(f"{self.story.description}\n\n")
        
        if self.story.author:
            md_parts.append(f"*von {self.story.author}*\n\n")
        
        md_parts.append(f"**Start:** Abschnitt {self.story.start_section_id}\n\n")
        md_parts.append("---\n\n")
        
        # Sortiere Sections nach ID
        sorted_sections = sorted(self.story.sections.items(), key=lambda x: x[0])
        
        for section_id, section in sorted_sections:
            md_parts.append(f"## [{section_id}] {section.title}\n\n")
            md_parts.append(f"{section.content}\n\n")
            
            if section.image_prompt:
                md_parts.append(f"🎨 *Bild-Prompt: {section.image_prompt}*\n\n")
            
            if section.hints:
                md_parts.append("💡 **Hinweise:**\n")
                for hint in section.hints:
                    md_parts.append(f"- {hint}\n")
                md_parts.append("\n")
            
            if section.choices:
                md_parts.append("**Entscheidungen:**\n\n")
                for choice in section.choices:
                    label = f"{choice.label}) " if choice.label else "- "
                    md_parts.append(f"{label}{choice.text} → `{choice.next_section_id}`\n")
                md_parts.append("\n")
            else:
                md_parts.append("**📖 ENDE 📖**\n\n")
            
            md_parts.append("---\n\n")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(''.join(md_parts))
