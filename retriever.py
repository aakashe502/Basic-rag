
import numpy as np
from embedding import get_embedding as embed
def retrieve(question, chunks):

    question_words = question.lower().split()

    scores = []

    for chunk in chunks:

        score = 0

        for word in question_words:

            if word in chunk.lower():
                score += 1

        scores.append((score, chunk))

    scores.sort(reverse=True)

    return [chunk for score, chunk in scores[:3]]

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
def embeddingretrieve(question, chunks, embeddings, top_k=3):

    question_embedding = embed(question)

    scores = []

    for chunk, embedding in zip(chunks, embeddings):

        score = cosine_similarity(
            question_embedding,
            embedding
        )

        scores.append((score, chunk))

    scores.sort(reverse=True)

    return [chunk for score, chunk in scores[:top_k]]