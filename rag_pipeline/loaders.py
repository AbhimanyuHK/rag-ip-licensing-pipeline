import pdfplumber
import docx

def load_file(path):
    if path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    if path.endswith(".docx"):
        doc = docx.Document(path)
        return "\n".join(p.text for p in doc.paragraphs)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
