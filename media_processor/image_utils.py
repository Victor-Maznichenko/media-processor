from PIL import Image, ImageFilter

def apply_blur_filter(input_path: str, output_path: str, radius: int = 2) -> None:
    """
    Applies a Gaussian blur filter to an image.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the blurred image.
    :param radius: The radius of the blur.
    """
    image = Image.open(input_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    blurred_image.save(output_path)
