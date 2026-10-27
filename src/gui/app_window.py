import tkinter as tk
from tkinter import filedialog, messagebox
from src.config import (
    APP_TITLE, WINDOW_SIZE, BG_COLOR,
    PRIMARY_BTN_COLOR, SECONDARY_BTN_COLOR, DANGER_BTN_COLOR
)
from src.core.validator import validate_image_files
from src.core.converter import generate_pdf
from src.gui.components import FileListBox

class PixelBindApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BG_COLOR)
        self.selected_files: list[str] = []

        tk.Label(
            root, text="PixelBind: PNG to PDF Converter",
            font=("Arial", 14, "bold"), bg=BG_COLOR
        ).pack(pady=(15, 5))

        self.file_list = FileListBox(root)
        self.file_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(root, bg=BG_COLOR)
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame, text="Add PNGs", command=self.add_files,
            bg=SECONDARY_BTN_COLOR, fg="white", width=14
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame, text="Clear List", command=self.clear_files,
            bg=DANGER_BTN_COLOR, fg="white", width=14
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            root, text="Convert & Save PDF", command=self.convert,
            bg=PRIMARY_BTN_COLOR, fg="white", font=("Arial", 10, "bold"), width=30, pady=5
        ).pack(pady=15)

        self.status_var = tk.StringVar(value="Ready. Select PNG files to begin.")
        tk.Label(
            root, textvariable=self.status_var, fg="gray", bg=BG_COLOR, font=("Arial", 9)
        ).pack(side=tk.BOTTOM, pady=5)

    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select PNG Images",
            filetypes=[("PNG Images", "*.png"), ("All Images", "*.png;*.jpg;*.jpeg")]
        )
        if not files:
            return

        valid, errors = validate_image_files(list(files))
        self.selected_files.extend(valid)
        self.file_list.update_files(self.selected_files)
        self.status_var.set(f"{len(self.selected_files)} valid file(s) queued.")

        if errors:
            messagebox.showwarning("Skipped Files", "\n".join(errors))

    def clear_files(self):
        self.selected_files.clear()
        self.file_list.update_files([])
        self.status_var.set("Queue cleared.")

    def convert(self):
        if not self.selected_files:
            messagebox.showwarning("No Files", "Please add at least one PNG image first.")
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Document", "*.pdf")],
            title="Save Output PDF As"
        )
        if not output_path:
            return

        try:
            generate_pdf(self.selected_files, output_path)
            self.status_var.set(f"Saved: {output_path}")
            messagebox.showinfo("Success", f"PDF created successfully!\n{output_path}")
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))