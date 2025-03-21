import os
import tempfile
import pytest
from media_processor import pdf_utils


def test_merge_pdfs():
    # Для тестирования можно создать временные PDF-файлы с помощью PyPDF2
    temp_pdf1 = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    temp_pdf2 = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    output_pdf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)

    # Создаем пустые PDF-файлы
    from PyPDF2 import PdfWriter
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(temp_pdf1.name, "wb") as f:
        writer.write(f)
    with open(temp_pdf2.name, "wb") as f:
        writer.write(f)

    pdf_utils.merge_pdfs([temp_pdf1.name, temp_pdf2.name], output_pdf.name)
    assert os.path.exists(output_pdf.name)

    # Очистка временных файлов
    os.remove(temp_pdf1.name)
    os.remove(temp_pdf2.name)
    os.remove(output_pdf.name)
