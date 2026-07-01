from loader import load_documents
from chunker import chunk_text
from embedding import get_embedding
from metadata import ChunkMetadata


class Indexer:

    def __init__(self, vector_store):

        self.vector_store = vector_store
    ...
    def build(self, folder):

        documents = load_documents(folder)

        chunk_id = 0

        for document in documents:

            chunks = chunk_text(document["text"])

            for chunk in chunks:

                metadata = ChunkMetadata(

                    chunk_id=chunk_id,

                    document_name=document["name"],

                    text=chunk
                )

                embedding = get_embedding(chunk)

                self.vector_store.add(
                    embedding,
                    metadata
                )

                chunk_id += 1