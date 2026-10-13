from pathlib import Path

from tablestats import read_rows, count_types, total_minutes, to_csv


if __name__ == "__main__":
    folder = Path(__file__).parent
    path = input().strip()

    with open(folder / path, encoding="utf-8") as table:
        rows = read_rows(table)

    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(f"{total_minutes(rows, 'ошибка'):.1f}")

    with open(folder / "summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))
