from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def extract_license(chunks):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
Extract IP licensing terms and return valid JSON:
{text}
"""
    )
    combined_text = "\n".join(chunks[:5])
    response = llm.predict(prompt.format(text=combined_text))
    return response
