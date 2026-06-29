import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dimension):
        self.index=faiss.IndexFlatL2(embedding_dimension)
        self.chunks=[]
        
    def add(self, chunk, embedding):
        embeddings=np.array(
            embedding,
            dtype=np.float32
        )
        self.index.add(embeddings)
        self.chunks.extend(chunk)
    
    def search(self, query_embedding, top_k=3):

        query_embedding = np.array(query_embedding, dtype=np.float32)

        # Convert from (384,) -> (1,384)
        query_embedding = np.expand_dims(query_embedding, axis=0)

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results
        