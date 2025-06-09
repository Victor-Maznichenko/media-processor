import os
import tempfile
import pytest
from media_processor import pdf_utils
from PyPDF2 import PdfWriter


def test_merge_pdfs():
    # Создаем временные файлы с ручным управлением удалением
    temp_pdf1 = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    temp_pdf1.close()  # Закрываем файл сразу после создания
    temp_pdf2 = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    temp_pdf2.close()
    output_pdf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    output_pdf.close()

    try:
        # Создаем пустые PDF-файлы
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)

        # Записываем в первый файл
        with open(temp_pdf1.name, "wb") as f:
            writer.write(f)

        # Записываем во второй файл
        with open(temp_pdf2.name, "wb") as f:
            writer.write(f)

        # Объединяем PDF-файлы
        pdf_utils.merge_pdfs([temp_pdf1.name, temp_pdf2.name], output_pdf.name)
        assert os.path.exists(output_pdf.name)

    finally:
        # Гарантированная очистка временных файлов
        if os.path.exists(temp_pdf1.name):
            os.remove(temp_pdf1.name)
        if os.path.exists(temp_pdf2.name):
            os.remove(temp_pdf2.name)
        if os.path.exists(output_pdf.name):
            os.remove(output_pdf.name)