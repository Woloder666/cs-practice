import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    array = np.asarray(values, dtype=float)
    return array.reshape(-1, width).round(6).tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    return array[np.ix_(rows, columns)].round(6).tolist()
