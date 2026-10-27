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


def column_means(matrix: list[list[float]]) -> list[float]:
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    return array.mean(axis=0).round(6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return 0.0
    values = array[:, column]
    return round(float(values.max() - values.min()), 6)


if __name__ == "__main__":
    assert reshape_rows([1, 2, 3], 2) == []
    assert column_means([]) == []
    assert column_range([], 0) == 0.0

    print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
    print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 2], [1, 2]))
    print(column_means([[1, 2], [3, 4], [5, 6]]))
    print(column_range([[1, 2], [5, 7]], 1))
