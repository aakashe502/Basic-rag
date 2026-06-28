from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
)

def ask_llm(context, question):

    prompt = f"""
        Use ONLY the context below.

        Context:
        {context}

        Question:
        {question}

        If answer isn't present say
        "I don't know."
        """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                 "role":"user",
                "content":prompt
            }
                ]
        )

    return response.choices[0].message.content