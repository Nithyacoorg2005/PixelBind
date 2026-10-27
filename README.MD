# PixelBind — PNG to PDF Utility

**PixelBind** is a lightweight Python desktop utility that converts single or multiple PNG images into a clean, multi-page PDF document. It automatically handles PNG transparency (`RGBA`) by flattening the alpha channel onto a solid white `RGB` background before compilation.

## Features
- **Batch Conversion:** Merge multiple PNG images into a single multi-page PDF.
- **Alpha Channel Handling:** Automatically composites transparent PNGs onto a crisp white background.
- **Desktop GUI:** Built-in interface using `Tkinter` for quick file selection, queue management, and export.
- **Offline & Lightweight:** Runs completely locally using Python's `Pillow` library.

## Tech Stack
- **Language:** Python 3.x
- **Image Processing:** Pillow (`PIL`)
- **Frontend GUI:** Tkinter
- **Testing:** Pytest

## Project Structure
    PixelBind/
    ├── main.py                  # Application entry point
    ├── requirements.txt         # Python dependencies
    ├── README.md                # Project documentation
    ├── .gitignore               # Ignored cache and temp files
    ├── src/
    │   ├── config.py            # App constants & settings
    │   ├── core/
    │   │   ├── converter.py     # Alpha-flattening & PDF generation
    │   │   └── validator.py     # File integrity & format checks
    │   └── gui/
    │       ├── app_window.py    # Main Tkinter window layout
    │       └── components.py    # Reusable UI widgets
    ├── sample_data/             # Test input PNGs & output PDFs
    └── tests/                   # Unit tests (test_converter.py)

## Quick Start

1. **Clone the repository:**
   git clone [https://github.com/Nithyacoorg2005/PixelBind.git]
   cd PixelBind

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Run the application:**
   python main.py

## Running Tests
To verify the conversion engine and alpha-flattening logic, run:

    pytest

## License
MIT License — free for academic and personal use.