from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_list: list, output_path: str) -> None:
    """
    Merges multiple PDF files into a single PDF.

    :param pdf_list: List of PDF file paths.
    :param output_path: Path to save the merged PDF.
    """
    pdf_writer = PdfWriter()
    for pdf in pdf_list:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as out_file:
        pdf_writer.write(out_file)
