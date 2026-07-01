from embedding import get_embedding_dimension
from vector_store import VectorStore
from indexer import Indexer
from rag import RAG
from llm import GroqLLM

embedding_dimension = get_embedding_dimension()

vector_store = VectorStore(
    embedding_dimension
)

indexer = Indexer(
    vector_store
)

indexer.build("documents")

llm = GroqLLM()

rag = RAG(
    vector_store,
    llm
)

while True:

    question = input("Ask: ")

    if question == "exit":
        break

    answer = rag.ask(question)

    print(answer)