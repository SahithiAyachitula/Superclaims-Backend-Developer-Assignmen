from PyPDF2 import PdfReader
from fastapi import UploadFile

async def extract_text_from_pdf(file: UploadFile) -> str:
    """Extracts text from uploaded PDF."""
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
    return text.strip()
