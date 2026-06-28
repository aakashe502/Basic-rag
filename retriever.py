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