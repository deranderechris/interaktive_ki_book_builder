#!/usr/bin/env python3
"""
Tkinter GUI for the Interactive Book Builder.
"""

import tkinter as tk
from tkinter import filedialog, messagebox

from book_builder import InteractiveBook


class BookBuilderGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interactive Book Builder")
        self.geometry("900x600")
        self.resizable(True, True)

        self.book = None
        self.chapters = []

        self._build_ui()

    def _build_ui(self):
        # Top: book meta
        meta_frame = tk.LabelFrame(self, text="Book")
        meta_frame.pack(fill=tk.X, padx=10, pady=8)

        tk.Label(meta_frame, text="Title").grid(row=0, column=0, sticky="w", padx=6, pady=4)
        self.title_entry = tk.Entry(meta_frame, width=40)
        self.title_entry.grid(row=0, column=1, sticky="w", padx=6, pady=4)

        tk.Label(meta_frame, text="Author").grid(row=0, column=2, sticky="w", padx=6, pady=4)
        self.author_entry = tk.Entry(meta_frame, width=30)
        self.author_entry.grid(row=0, column=3, sticky="w", padx=6, pady=4)

        # Middle: chapter editor
        editor_frame = tk.LabelFrame(self, text="Chapter")
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        tk.Label(editor_frame, text="Chapter title").grid(row=0, column=0, sticky="w", padx=6, pady=4)
        self.chapter_title_entry = tk.Entry(editor_frame, width=40)
        self.chapter_title_entry.grid(row=0, column=1, sticky="w", padx=6, pady=4)

        tk.Label(editor_frame, text="Image path (optional)").grid(row=0, column=2, sticky="w", padx=6, pady=4)
        self.image_path_entry = tk.Entry(editor_frame, width=35)
        self.image_path_entry.grid(row=0, column=3, sticky="w", padx=6, pady=4)
        tk.Button(editor_frame, text="Browse", command=self._browse_image).grid(
            row=0, column=4, sticky="w", padx=6, pady=4
        )

        tk.Label(editor_frame, text="Chapter content").grid(row=1, column=0, sticky="nw", padx=6, pady=4)
        self.chapter_content_text = tk.Text(editor_frame, height=12, width=80, wrap="word")
        self.chapter_content_text.grid(row=1, column=1, columnspan=4, sticky="nsew", padx=6, pady=4)

        editor_frame.rowconfigure(1, weight=1)
        editor_frame.columnconfigure(3, weight=1)

        button_row = tk.Frame(editor_frame)
        button_row.grid(row=2, column=1, columnspan=4, sticky="w", padx=6, pady=6)
        tk.Button(button_row, text="Add chapter", command=self._add_chapter).pack(side=tk.LEFT, padx=4)
        tk.Button(button_row, text="Remove selected", command=self._remove_selected).pack(side=tk.LEFT, padx=4)

        # Right: chapter list
        list_frame = tk.LabelFrame(self, text="Chapters")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        self.chapter_list = tk.Listbox(list_frame, height=6)
        self.chapter_list.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        # Bottom: actions
        action_frame = tk.Frame(self)
        action_frame.pack(fill=tk.X, padx=10, pady=8)

        tk.Button(action_frame, text="Export JSON", command=self._export_json).pack(side=tk.LEFT, padx=4)
        tk.Button(action_frame, text="Export HTML", command=self._export_html).pack(side=tk.LEFT, padx=4)
        tk.Button(action_frame, text="Reset", command=self._reset).pack(side=tk.LEFT, padx=4)

        self.status_var = tk.StringVar(value="Ready")
        status_label = tk.Label(action_frame, textvariable=self.status_var, anchor="w")
        status_label.pack(side=tk.RIGHT, fill=tk.X, expand=True)

    def _browse_image(self):
        path = filedialog.askopenfilename(
            title="Select image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.webp"), ("All files", "*")],
        )
        if path:
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, path)

    def _add_chapter(self):
        title = self.chapter_title_entry.get().strip()
        content = self.chapter_content_text.get("1.0", tk.END).strip()
        image = self.image_path_entry.get().strip() or None

        if not title:
            messagebox.showerror("Missing title", "Please enter a chapter title.")
            return
        if not content:
            messagebox.showerror("Missing content", "Please enter chapter content.")
            return

        self.chapters.append({"title": title, "content": content, "image": image})
        self.chapter_list.insert(tk.END, title)

        self.chapter_title_entry.delete(0, tk.END)
        self.chapter_content_text.delete("1.0", tk.END)
        self.image_path_entry.delete(0, tk.END)

        self.status_var.set(f"Added chapter: {title}")

    def _remove_selected(self):
        selection = self.chapter_list.curselection()
        if not selection:
            return
        index = selection[0]
        removed = self.chapters.pop(index)
        self.chapter_list.delete(index)
        self.status_var.set(f"Removed chapter: {removed['title']}")

    def _create_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()

        if not title or not author:
            messagebox.showerror("Missing data", "Please enter both title and author.")
            return None

        if not self.chapters:
            messagebox.showerror("No chapters", "Please add at least one chapter.")
            return None

        book = InteractiveBook(title=title, author=author)
        for chapter in self.chapters:
            book.add_chapter(chapter["title"], chapter["content"], chapter.get("image"))
        return book

    def _export_json(self):
        book = self._create_book()
        if not book:
            return
        path = filedialog.asksaveasfilename(
            title="Save JSON",
            defaultextension=".json",
            filetypes=[("JSON", "*.json")],
        )
        if not path:
            return
        book.save_to_json(path)
        self.status_var.set(f"Saved JSON: {path}")

    def _export_html(self):
        book = self._create_book()
        if not book:
            return
        path = filedialog.asksaveasfilename(
            title="Save HTML",
            defaultextension=".html",
            filetypes=[("HTML", "*.html")],
        )
        if not path:
            return
        book.save_to_html(path)
        self.status_var.set(f"Saved HTML: {path}")

    def _reset(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.chapter_title_entry.delete(0, tk.END)
        self.chapter_content_text.delete("1.0", tk.END)
        self.image_path_entry.delete(0, tk.END)
        self.chapter_list.delete(0, tk.END)
        self.chapters.clear()
        self.status_var.set("Ready")


def main():
    app = BookBuilderGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
