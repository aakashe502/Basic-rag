from loader import load_document
from chunker import chunk_text
from retriever import retrieve
from llm import ask_llm

text = load_document("documents/company.txt")

chunks = chunk_text(text)

question = input("Ask: ")

results = retrieve(question, chunks)

context = "\n".join(results)

answer = ask_llm(context, question)

print(answer)