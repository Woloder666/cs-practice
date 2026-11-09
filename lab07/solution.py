import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    data = np.asarray(values, dtype=float)
    table = data.reshape(-1, width)
    return np.round(table, 6).tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix: 
        return []

    data = np.asarray(matrix, dtype=float)
    selected = data[np.ix_(rows, columns)]
    return np.round(selected, 6).tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix: 
        return []
        
    data = np.asarray(matrix, dtype=float)
    means = data.mean(axis=0)
    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix: 
        return 0.0
    data = np.asarray(matrix, dtype=float)

    values = data[:, column]
    return float(np.round(values.max() - values.min(), 6))
