def winner(names: list[str], scores: list[float]) -> str:
    best = 0

    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i

    return names[best]


def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0

    total = 0

    for score in scores:
        total += score

    return round(total / len(scores), 2)
