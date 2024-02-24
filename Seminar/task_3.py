'''
Задание №3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
'''

data = (42, 73, 3.14, 'Hello World!', None, True, 'Text', 100500.2, False)

dict_data = {}

for item in data:
    item_type = type(item)
    if item_type not in dict_data:
        dict_data[item_type] = [item]
    dict_data[item_type].append(item)

print(dict_data)