# app/ocr.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(file_stream):
    """
    Extrai texto de um PDF usando PyMuPDF.
    Se a página for imagem, aplica OCR com pytesseract.
    """
    try:
        doc = fitz.open(stream=file_stream.read(), filetype="pdf")
    except Exception as e:
        return f"Erro ao abrir o PDF: {e}"

    all_text = []

    for page_num in range(len(doc)):
        try:
            page = doc.load_page(page_num)
            text = page.get_text()

            if not text.strip():
                pix = page.get_pixmap(dpi=300)
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                text = pytesseract.image_to_string(img)

            all_text.append(text)
        except Exception as e:
            all_text.append(f"[Erro na página {page_num}: {e}]")

    return "\n".join(all_text)
