# Словари, dict
# Создание словаря
# Разберём на примерах.
# ✔ dict(x) — создаём словарь
# ✔ {key: value} — тоже создаём словарь
a = {'one': 42, 'two': 3.14, 'ten': 'Hello World!'}
b = dict(one=42, two=3.14, ten='Hello World!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello World!')])
print(a == b == c)