'''
Задание №5
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
'''

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unique_list = []

for n, item in enumerate(data, 1):
    if item % 2:
        unique_list.append(n)

print(unique_list)