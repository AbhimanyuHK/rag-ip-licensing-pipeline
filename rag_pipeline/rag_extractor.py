# rag_pipeline/rag_extractor.py

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

def extract(context: str) -> dict:
    llm = ChatOllama(
        model="llama3",
        base_url="http://127.0.0.1:11434"
    )

    prompt = ChatPromptTemplate.from_template("""
You are a legal contract extraction AI.

Extract IP licensing, royalties, and revenue share details
from the following content and return STRICT JSON.

Content:
{context}

JSON format:
{{
  "ip_owner": "",
  "licensee": "",
  "royalty_percentage": "",
  "revenue_share": "",
  "territory": "",
  "duration": "",
  "payment_terms": ""
}}
""")

    chain = prompt | llm
    response = chain.invoke({"context": context})

    return response.content
