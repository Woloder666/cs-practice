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
