import os
import tkinter as tk

class FileListBox(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(
            self,
            yscrollcommand=self.scrollbar.set,
            width=55,
            height=8,
            font=("Consolas", 9)
        )
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def update_files(self, file_paths: list[str]):
        self.listbox.delete(0, tk.END)
        for idx, path in enumerate(file_paths, start=1):
            self.listbox.insert(tk.END, f"{idx}. {os.path.basename(path)}")