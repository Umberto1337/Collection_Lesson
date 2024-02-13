'''
Задание
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в верхнем регистре в остальных случаях
'''

data = input("Введите данные: ")

if data.isdigit():
    result = int(data)
elif data.replace('.', '', 1).replace('-', '', 1).isdigit() and data.count('.') <= 1:
    result = float(data)
elif not data.islower():
    result = data.lower()
else:
    result = data.upper()
    
print(f'Результат: {result}\t{type(result)}')