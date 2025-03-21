from PIL import Image

def add_watermark(image_path: str, watermark_path: str, output_path: str, position: tuple = (0, 0)) -> None:
    """
    Adds a watermark image over the original image.

    :param image_path: Path to the original image.
    :param watermark_path: Path to the watermark image.
    :param output_path: Path to save the watermarked image.
    :param position: Tuple (x, y) for the watermark position.
    """
    base_image = Image.open(image_path).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")
    # Создаем прозрачный слой для объединения
    layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    # Используем watermark как маску для сохранения прозрачности
    layer.paste(watermark, position, mask=watermark)
    watermarked_image = Image.alpha_composite(base_image, layer)
    watermarked_image.convert("RGB").save(output_path)
