from embedding import get_embedding


class RAG:

    def __init__(
        self,
        vector_store,
        llm
    ):

        self.vector_store = vector_store
        self.llm = llm

    def ask(
        self,
        question,
        top_k=3
    ):

        question_embedding = get_embedding(question)

        retrieved_chunks = self.vector_store.search(
            question_embedding,
            top_k
        )

        print("\nRetrieved Chunks:")
        print("=" * 50)

        for chunk in retrieved_chunks:
            print(f"Document : {chunk.document_name}")
            print(f"Chunk ID : {chunk.chunk_id}")
            print(f"Content  : {chunk.text}")
            print("-" * 50)

        context = ""

        for chunk in retrieved_chunks:

            context += f"""



        Document:
        {chunk.document_name}

        Content:
        {chunk.text}

        ----------------------------------------

        """

        prompt = f"""
        You are a helpful AI assistant.

        Answer ONLY from the provided context.

        If the answer is not present,
        reply:

        "I couldn't find the answer in the documents."

        Context:

        {context}

        Question:

        {question}

        Answer:
        """

        answer = self.llm.generate(prompt)

        return answer