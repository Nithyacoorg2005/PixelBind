import os
from PIL import Image
from src.core.converter import flatten_alpha, generate_pdf

def test_flatten_rgba_to_rgb():
    rgba_img = Image.new("RGBA", (100, 100), (255, 0, 0, 128))
    flattened = flatten_alpha(rgba_img)
    assert flattened.mode == "RGB"
    assert flattened.size == (100, 100)

def test_generate_pdf(tmp_path):
    img_path = tmp_path / "sample.png"
    pdf_path = tmp_path / "output.pdf"
    Image.new("RGBA", (50, 50), (0, 255, 0, 255)).save(img_path)

    generate_pdf([str(img_path)], str(pdf_path))
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 0