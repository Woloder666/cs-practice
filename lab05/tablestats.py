def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        fields = line.split(",")
        for i in range(len(fields)):
            fields[i] = fields[i].strip()

        if header is None:
            header = fields
            continue

        if len(fields) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i]] = fields[i]
        rows.append(row)

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}

    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1

    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row["тип"] == kind:
            try:
                minutes = float(row["минуты"].replace(",", "."))
            except ValueError:
                continue
            total += minutes

    return round(total, 1)


def to_csv(counts: dict) -> str:
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += kind + "," + str(counts[kind]) + "\n"

    return result
