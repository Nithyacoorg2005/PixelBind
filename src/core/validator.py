import os
from PIL import Image
from src.config import VALID_EXTENSIONS

def validate_image_files(file_paths: list[str]) -> tuple[list[str], list[str]]:
    valid_files = []
    errors = []

    for path in file_paths:
        if not os.path.exists(path):
            errors.append(f"Missing file: {os.path.basename(path)}")
            continue
        if not path.lower().endswith(VALID_EXTENSIONS):
            errors.append(f"Unsupported format: {os.path.basename(path)}")
            continue
        try:
            with Image.open(path) as img:
                img.verify()
            valid_files.append(path)
        except Exception:
            errors.append(f"Corrupted image: {os.path.basename(path)}")

    return valid_files, errors