from loader import load_document
from chunker import chunk_text
from embedding import get_embedding
from retriever import retrieve,embeddingretrieve
from llm import ask_llm


class BasicRAG:

    def __init__(self, document_path):

        print("Loading document...")

        self.document = load_document(document_path)

        print("Chunking document...")

        self.chunks = chunk_text(self.document)

        print(f"Created {len(self.chunks)} chunks")

        print("Generating embeddings...")

        self.embeddings = [
            get_embedding(chunk)
            for chunk in self.chunks
        ]

        print("Ready!\n")

    def ask(self, question):

        retrieved_chunks = embeddingretrieve(
            question,
            self.chunks,
            self.embeddings
        )

        context = "\n\n".join(retrieved_chunks)

        answer = ask_llm(context, question)

        return answer