from io import StringIO

from tablestats import read_rows, count_types, total_minutes, to_csv


assert read_rows([]) == []
assert read_rows(["", "  "]) == []
assert read_rows(["тип,минуты"]) == []

lines = ["\n", " дата , тип , минуты \n", " d , ошибка , 0.4 \n",
         "", "битая строка", "d,ошибка,1,лишнее"]
expected = [{"дата": "d", "тип": "ошибка", "минуты": "0.4"}]
assert read_rows(lines) == expected
assert read_rows(StringIO("\n".join(lines))) == expected
assert read_rows(iter(lines)) == expected

rows = [{"тип": "ошибка", "минуты": "0,4"},
        {"тип": "ошибка", "минуты": "1.26"},
        {"тип": "ошибка", "минуты": "нет числа"},
        {"тип": "запуск", "минуты": "5"}]
assert count_types(rows) == {"ошибка": 3, "запуск": 1}
assert count_types([]) == {}
assert total_minutes(rows, "ошибка") == 1.7
assert total_minutes(rows, "выгрузка") == 0.0
assert total_minutes([], "ошибка") == 0.0
assert to_csv({}) == "тип,количество\n"
assert to_csv({"ошибка": 3, "запуск": 1}) == "тип,количество\nзапуск,1\nошибка,3\n"

print("Все проверки пройдены")
