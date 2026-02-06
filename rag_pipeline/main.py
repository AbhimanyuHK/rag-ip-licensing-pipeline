import os, json
from loaders import load_pdf, load_docx, load_txt
from chunker import chunk_text
from rag_extractor import extract_license

INPUT_DIR = "input_contracts"
OUTPUT_DIR = "output_json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    path = f"{INPUT_DIR}/{file}"

    if file.endswith(".pdf"):
        text = load_pdf(path)
    elif file.endswith(".docx"):
        text = load_docx(path)
    else:
        text = load_txt(path)

    chunks = chunk_text(text)
    result = extract_license(chunks)

    with open(f"{OUTPUT_DIR}/{file}.json", "w") as f:
        f.write(result)
