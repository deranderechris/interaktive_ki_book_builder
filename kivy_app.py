#!/usr/bin/env python3
"""
Kivy GUI for Android (and desktop) to build interactive books.
"""

import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import webbrowser

from book_builder import InteractiveBook


class BookBuilderRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        Window.minimum_width = 720
        Window.minimum_height = 640

        self.chapters = []
        self._build_ui()

    def _build_ui(self):
        # Book meta
        meta = GridLayout(cols=2, padding=8, spacing=6, size_hint_y=None)
        meta.bind(minimum_height=meta.setter("height"))

        meta.add_widget(Label(text="Title", size_hint_x=0.3))
        self.title_input = TextInput(multiline=False)
        meta.add_widget(self.title_input)

        meta.add_widget(Label(text="Author", size_hint_x=0.3))
        self.author_input = TextInput(multiline=False)
        meta.add_widget(self.author_input)

        self.add_widget(meta)

        # Chapter editor
        editor = GridLayout(cols=2, padding=8, spacing=6, size_hint_y=None)
        editor.bind(minimum_height=editor.setter("height"))

        editor.add_widget(Label(text="Chapter title", size_hint_x=0.3))
        self.chapter_title_input = TextInput(multiline=False)
        editor.add_widget(self.chapter_title_input)

        editor.add_widget(Label(text="Image path", size_hint_x=0.3))
        image_row = BoxLayout(orientation="horizontal", spacing=6)
        self.image_path_input = TextInput(multiline=False)
        image_row.add_widget(self.image_path_input)
        image_row.add_widget(Button(text="Browse", size_hint_x=0.3, on_release=self._browse_image))
        editor.add_widget(image_row)

        editor.add_widget(Label(text="Chapter content", size_hint_x=0.3))
        self.chapter_content_input = TextInput(multiline=True, size_hint_y=None, height=160)
        editor.add_widget(self.chapter_content_input)

        self.add_widget(editor)

        # Chapter actions
        actions = BoxLayout(orientation="horizontal", padding=8, spacing=6, size_hint_y=None, height=44)
        actions.add_widget(Button(text="Add chapter", on_release=self._add_chapter))
        actions.add_widget(Button(text="Remove last", on_release=self._remove_last))
        actions.add_widget(Button(text="Reset", on_release=self._reset))
        self.add_widget(actions)

        # Chapter list
        list_label = Label(text="Chapters", size_hint_y=None, height=24)
        self.add_widget(list_label)

        self.chapters_list = GridLayout(cols=1, spacing=4, size_hint_y=None)
        self.chapters_list.bind(minimum_height=self.chapters_list.setter("height"))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.chapters_list)
        self.add_widget(scroll)

        # Export actions
        export_actions = BoxLayout(orientation="horizontal", padding=8, spacing=6, size_hint_y=None, height=44)
        export_actions.add_widget(Button(text="Export JSON", on_release=self._export_json))
        export_actions.add_widget(Button(text="Export HTML", on_release=self._export_html))
        export_actions.add_widget(Button(text="Preview HTML", on_release=self._preview_html))
        self.add_widget(export_actions)

    def _browse_image(self, _instance):
        chooser = FileChooserListView(filters=["*.png", "*.jpg", "*.jpeg", "*.gif", "*.webp"], path="/")

        def select_path(_btn):
            if chooser.selection:
                self.image_path_input.text = chooser.selection[0]
            popup.dismiss()

        layout = BoxLayout(orientation="vertical", spacing=6, padding=8)
        layout.add_widget(chooser)
        buttons = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=6)
        buttons.add_widget(Button(text="Select", on_release=select_path))
        buttons.add_widget(Button(text="Cancel", on_release=lambda _btn: popup.dismiss()))
        layout.add_widget(buttons)

        popup = Popup(title="Select image", content=layout, size_hint=(0.9, 0.9))
        popup.open()

    def _add_chapter(self, _instance):
        title = self.chapter_title_input.text.strip()
        content = self.chapter_content_input.text.strip()
        image = self.image_path_input.text.strip() or None

        if not title:
            self._show_message("Missing title", "Please enter a chapter title.")
            return
        if not content:
            self._show_message("Missing content", "Please enter chapter content.")
            return

        self.chapters.append({"title": title, "content": content, "image": image})
        self._refresh_chapter_list()

        self.chapter_title_input.text = ""
        self.chapter_content_input.text = ""
        self.image_path_input.text = ""

    def _remove_last(self, _instance):
        if not self.chapters:
            return
        self.chapters.pop()
        self._refresh_chapter_list()

    def _reset(self, _instance):
        self.title_input.text = ""
        self.author_input.text = ""
        self.chapter_title_input.text = ""
        self.chapter_content_input.text = ""
        self.image_path_input.text = ""
        self.chapters = []
        self._refresh_chapter_list()

    def _refresh_chapter_list(self):
        self.chapters_list.clear_widgets()
        if not self.chapters:
            self.chapters_list.add_widget(Label(text="No chapters yet", size_hint_y=None, height=24))
            return
        for index, chapter in enumerate(self.chapters, 1):
            label = Label(text=f"{index}. {chapter['title']}", size_hint_y=None, height=24)
            self.chapters_list.add_widget(label)

    def _create_book(self):
        title = self.title_input.text.strip()
        author = self.author_input.text.strip()

        if not title or not author:
            self._show_message("Missing data", "Please enter both title and author.")
            return None
        if not self.chapters:
            self._show_message("No chapters", "Please add at least one chapter.")
            return None

        book = InteractiveBook(title=title, author=author)
        for chapter in self.chapters:
            book.add_chapter(chapter["title"], chapter["content"], chapter.get("image"))
        return book

    def _choose_save_path(self, title, default_name, extension, on_save):
        start_dir = App.get_running_app().user_data_dir or os.getcwd()
        chooser = FileChooserListView(path=start_dir)
        filename_input = TextInput(text=default_name, multiline=False, size_hint_y=None, height=36)

        def do_save(_btn):
            if chooser.selection:
                selected = chooser.selection[0]
                if os.path.isdir(selected):
                    directory = selected
                else:
                    directory = os.path.dirname(selected)
                    if not filename_input.text.strip():
                        filename_input.text = os.path.basename(selected)
            else:
                directory = chooser.path

            name = filename_input.text.strip()
            if not name:
                self._show_message("Missing filename", "Please enter a filename.")
                return

            path = os.path.join(directory, name)
            if not path.lower().endswith(extension):
                path += extension
            if os.path.exists(path):
                self._confirm_overwrite(path, on_save, popup)
                return
            popup.dismiss()
            on_save(path)

        layout = BoxLayout(orientation="vertical", spacing=6, padding=8)
        layout.add_widget(chooser)
        layout.add_widget(Label(text="Filename", size_hint_y=None, height=24))
        layout.add_widget(filename_input)
        buttons = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=6)
        buttons.add_widget(Button(text="Save", on_release=do_save))
        buttons.add_widget(Button(text="Cancel", on_release=lambda _btn: popup.dismiss()))
        layout.add_widget(buttons)

        popup = Popup(title=title, content=layout, size_hint=(0.9, 0.9))
        popup.open()

    def _confirm_overwrite(self, path, on_save, parent_popup):
        def confirm(_btn):
            overwrite_popup.dismiss()
            parent_popup.dismiss()
            on_save(path)

        content = BoxLayout(orientation="vertical", padding=8, spacing=6)
        content.add_widget(Label(text=f"File exists:\n{path}\nOverwrite?"))
        buttons = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=6)
        buttons.add_widget(Button(text="Overwrite", on_release=confirm))
        buttons.add_widget(Button(text="Cancel", on_release=lambda _btn: overwrite_popup.dismiss()))
        content.add_widget(buttons)

        overwrite_popup = Popup(title="Confirm overwrite", content=content, size_hint=(0.8, 0.4))
        overwrite_popup.open()

    def _export_json(self, _instance):
        book = self._create_book()
        if not book:
            return
        self._choose_save_path(
            title="Save JSON",
            default_name="book.json",
            extension=".json",
            on_save=lambda path: self._save_book(book, path, "json"),
        )

    def _export_html(self, _instance):
        book = self._create_book()
        if not book:
            return
        self._choose_save_path(
            title="Save HTML",
            default_name="book.html",
            extension=".html",
            on_save=lambda path: self._save_book(book, path, "html"),
        )

    def _preview_html(self, _instance):
        book = self._create_book()
        if not book:
            return
        out_dir = App.get_running_app().user_data_dir or os.getcwd()
        path = os.path.join(out_dir, "preview_book.html")
        book.save_to_html(path)
        try:
            webbrowser.open(f"file://{path}")
            self._show_message("Preview", f"Opened preview:\n{path}")
        except Exception as exc:
            self._show_message("Preview failed", str(exc))

    def _save_book(self, book, path, kind):
        if kind == "json":
            book.save_to_json(path)
        else:
            book.save_to_html(path)
        self._show_message("Saved", f"Saved to: {path}")

    def _show_message(self, title, message):
        content = BoxLayout(orientation="vertical", padding=8, spacing=6)
        content.add_widget(Label(text=message))
        content.add_widget(Button(text="OK", size_hint_y=None, height=40, on_release=lambda _btn: popup.dismiss()))
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        popup.open()


class BookBuilderApp(App):
    def build(self):
        self.title = "Interactive Book Builder"
        return BookBuilderRoot()


def main():
    BookBuilderApp().run()


if __name__ == "__main__":
    main()
