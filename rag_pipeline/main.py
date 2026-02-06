import os, json
from loaders import load_file
from chunker import chunk_text
from rag_extractor import extract
from validator import parse_and_validate

def extract_with_retry(text, extract_fn, retries=3):
    last_error = None

    for _ in range(retries):
        output = extract_fn(text)
        try:
            return parse_and_validate(output)
        except ValueError as e:
            last_error = str(e)

    raise RuntimeError(f"Extraction failed after retries: {last_error}")


INPUT_DIR = "input_contracts"
OUTPUT_DIR = "output_json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def execute():
    for file in os.listdir(INPUT_DIR):
        path = f"{INPUT_DIR}/{file}"
        text = load_file(path)
        chunks = chunk_text(text)
        out_path = f"{OUTPUT_DIR}/{file}.json"
        
        # result = extract(chunks)
        # with open(out_path, "w", encoding="utf-8") as f:
        #     f.write(result)

        license_obj = extract_with_retry(chunks, extract)

        with open(out_path, "w") as f:
            f.write(license_obj.model_dump_json(indent=2))

        print(f"Generated: {out_path}")


if __name__ == "__main__":
    execute()
