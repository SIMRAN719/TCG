import os
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
import fitz
def extract_text(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    try:
        if file_extension == '.pdf':
            return extract_text_from_pdf(file_path)
        elif file_extension in ['.docx', '.doc']:
            return extract_text_from_docx(file_path)
        elif file_extension == '.txt':
            return extract_text_from_txt(file_path)
        elif file_extension in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']:
            return extract_text_from_image(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  
        text += page.get_text()  

    return text

# def extract_text_from_pdf(file_path):
#     text = ''
#     with pdfplumber.open(file_path) as pdf:
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text
#     return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def extract_text_from_txt(file_path):
    text = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        texts = file.read()
        text+=texts
    return text

def extract_text_from_image(file_path):
    text = pytesseract.image_to_string(Image.open(file_path))
    return text

