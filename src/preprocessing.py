import os
import pdfplumber
import docx2txt
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

# --- PDF extraction ---


def extract_pdf_text(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"PDF extraction failed for {file_path}: {e}")
    return text.strip()

# --- OCR for scanned PDF ---


def ocr_pdf(file_path):
    text = ""
    try:
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"
    except Exception as e:
        print(f"OCR failed for {file_path}: {e}")
    return text.strip()

# --- DOCX extraction ---


def extract_docx_text(file_path):
    try:
        return docx2txt.process(file_path).strip()
    except Exception as e:
        print(f"DOCX extraction failed for {file_path}: {e}")
        return ""

# --- OCR for images ---


def ocr_image(file_path):
    try:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img).strip()
    except Exception as e:
        print(f"Image OCR failed for {file_path}: {e}")
        return ""


# --- Process all files ---
for filename in os.listdir(RAW_DIR):
    file_path = os.path.join(RAW_DIR, filename)
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    output_path = os.path.join(PROCESSED_DIR, f"{name}_raw.txt")

    text = ""
    if ext == ".pdf":
        text = extract_pdf_text(file_path)
        if not text:
            text = ocr_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        text = extract_docx_text(file_path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        text = ocr_image(file_path)
    else:
        print(f"Skipping unsupported file type: {filename}")
        continue

    if text:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Processed: {filename} → {output_path}")
    else:
        print(f"No text extracted from {filename}")
