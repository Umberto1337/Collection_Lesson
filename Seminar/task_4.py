'''
Задание №4
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
'''

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
unique_list = [item for item in data if data.count(item) != 2]
print(unique_list)