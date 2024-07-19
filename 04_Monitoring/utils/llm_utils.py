import os
import uuid
from openai import OpenAI
import google.generativeai as genai


client = OpenAI(api_key=os.environ['OPENAI_API_KEY']) # Or , ETC 
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

# genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-1.5-flash')
 


def ask_llm(# google_model_name: str,  
            openai_model_name: str, 
            messages: list[dict], mock_answer: bool = False) -> str:
    if not mock_answer:
        # response = model.generate_content(
        #     messages=messages)
        response = client.chat.completions.create(
            model=openai_model_name,
            messages=messages,
            max_tokens=150
        ).choices[0].message.content.strip()
    else:
        response = 'hello' + str(uuid.uuid4())
    return response


def build_prompt(query: str, search_results: list[str]) -> str:
    prompt_template = """
        You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
        Use only the facts from the CONTEXT when answering the QUESTION.

        QUESTION: {question}

        CONTEXT: 
        {context}
        """.strip()

    context = ""
    
    for search_result in search_results:
        context = context + f"{search_result}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt
