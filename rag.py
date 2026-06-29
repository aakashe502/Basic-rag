from loader import load_document
from chunker import chunk_text
from embedding import get_embedding
from vector_store import VectorStore

from llm import ask_llm


class BasicRAG:

    def __init__(self, document_path):

        self.document = load_document(document_path)

        self.chunks = chunk_text(self.document)

        embeddings = [
            get_embedding(chunk)
            for chunk in self.chunks
        ]

        embedding_dimension = len(embeddings[0])

        self.vector_store = VectorStore(
            embedding_dimension
        )

        self.vector_store.add(
            self.chunks,
            embeddings
        )

    def ask(self, question):

        question_embedding = get_embedding(question)

        retrieved_chunks = self.vector_store.search(
            question_embedding,
            top_k=3
        )

        context = "\n".join(retrieved_chunks)

        return ask_llm(context, question)