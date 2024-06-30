import fitz  # PyMuPDF

def pdf_to_string(pdf_file) -> str: 
    pdf_stream = pdf_file.read()
    document = fitz.open(stream=pdf_stream, filetype="pdf")
    pdf_text = ""

    # acceess each page in the pdf file
    for page_num in range(document.page_count):
        page = document[page_num]
        pdf_text += page.get_text()

    return pdf_text

