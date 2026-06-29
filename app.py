from rag import BasicRAG

rag = BasicRAG("documents/company.txt")

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer = rag.ask(question)

    print("\nAnswer:")
    print(answer)