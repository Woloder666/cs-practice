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


def ranking(names: list[str], scores: list[float]) -> list[str]:
    result = names.copy()
    result_scores = scores.copy()

    for i in range(len(result_scores)):
        for j in range(i + 1, len(result_scores)):
            if result_scores[j] > result_scores[i]:
                result_scores[i], result_scores[j] = result_scores[j], result_scores[i]
                result[i], result[j] = result[j], result[i]

    return result


def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []

    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])

    return result
