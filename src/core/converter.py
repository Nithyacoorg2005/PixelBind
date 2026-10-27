from PIL import Image
from src.config import WHITE_RGB, DEFAULT_PDF_DPI

def flatten_alpha(img: Image.Image) -> Image.Image:
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        background = Image.new("RGB", img.size, WHITE_RGB)
        background.paste(img, mask=img.split()[3])
        return background
    return img.convert("RGB")

def generate_pdf(image_paths: list[str], output_path: str) -> None:
    if not image_paths:
        raise ValueError("No valid images provided for conversion.")

    processed_images = []
    for path in image_paths:
        with Image.open(path) as img:
            processed_images.append(flatten_alpha(img))

    processed_images[0].save(
        output_path,
        "PDF",
        resolution=DEFAULT_PDF_DPI,
        save_all=True,
        append_images=processed_images[1:]
    )