# rag_pipeline/rag_extractor.py

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

SCHEMA_INSTRUCTIONS = """
Return ONLY valid JSON matching this schema:

{
  "license_id": "string",
  "territory": ["string"],
  "term": "string | null",
  "royalty": {
    "rate": "number | null",
    "basis": "string | null",
    "evidence": "string | null"
  },
  "sub_licensing": "boolean | null",
  "status": "string"
}

Rules:
- Do not omit required fields
- Use null if value is missing
- Do not add extra keys
"""

PROMPT_OPEN = """
You are a legal contract extraction AI.

Extract IP licensing, royalties, and revenue share details
from the following content and return STRICT JSON.

Content:
{context}

""" + SCHEMA_INSTRUCTIONS

def extract(context: str) -> dict:
    llm = ChatOllama(
        model="mistral",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(PROMPT_OPEN)

    chain = prompt | llm
    response = chain.invoke({"context": context})

    return response.content
