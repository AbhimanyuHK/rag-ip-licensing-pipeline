import os, json
from loaders import load_file
from chunker import chunk_text
from rag_extractor import extract

INPUT_DIR = "input_contracts"
OUTPUT_DIR = "output_json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    path = f"{INPUT_DIR}/{file}"
    text = load_file(path)
    chunks = chunk_text(text)

    result = extract(chunks)

    out_path = f"{OUTPUT_DIR}/{file}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Generated: {out_path}")
