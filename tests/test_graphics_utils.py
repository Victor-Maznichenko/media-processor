import os
import tempfile
from PIL import Image
import pytest
from media_processor import graphics_utils

def test_add_watermark():
    # Создаем временное изображение и водяной знак
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
        base = Image.new("RGB", (200, 200), color="blue")
        base.save(temp_img.name)
        base_path = temp_img.name

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_wm:
        watermark = Image.new("RGBA", (50, 50), color=(255, 255, 255, 128))
        watermark.save(temp_wm.name)
        wm_path = temp_wm.name

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_out:
        output_path = temp_out.name

    graphics_utils.add_watermark(base_path, wm_path, output_path, position=(10, 10))
    assert os.path.exists(output_path)

    # Очистка временных файлов
    os.remove(base_path)
    os.remove(wm_path)
    os.remove(output_path)
