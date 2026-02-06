from langchain_ollama import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(
    model="mistral",
    temperature=0
)

PROMPT = """
You are a legal extraction engine.

Extract IP licensing details and return ONLY valid JSON.

Required fields:
- license_id
- territory
- term
- royalty.rate
- royalty.basis
- sub_licensing

Text:
{text}
"""

def extract(chunks):
    prompt = PromptTemplate(
        input_variables=["text"],
        template=PROMPT
    )
    return llm.invoke(prompt.format(text="\n".join(chunks)))
