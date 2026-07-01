import faiss
import numpy as np


class VectorStore:

    def __init__(self, embedding_dimension):

        self.index = faiss.IndexFlatL2(
            embedding_dimension
        )

        self.metadata = []

    def add(
        self,
        embedding,
        metadata
    ):

        embedding = np.array(
            embedding,
            dtype=np.float32
        ).reshape(1, -1)

        self.index.add(embedding)

        self.metadata.append(metadata)

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        ).reshape(1, -1)

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx != -1:

                results.append(
                    self.metadata[idx]
                )

        return results