import tkinter as tk
from src.gui.app_window import PixelBindApp

if __name__ == "__main__":
    root = tk.Tk()
    app = PixelBindApp(root)
    root.mainloop()