from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    return model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def get_embedding_dimension():
    return model.get_sentence_embedding_dimension()