'''
Задание №1
✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
'''
my_list = [13, 1, 5, 6, 7, 13, 1, 6, 9, 10]

# Вариант короткий
print(list(set(my_list))) 

# Вариант длинный
new_list = []  
for num in my_list:
    if num not in new_list:
        new_list.append(num)       
print(sorted(new_list))

# Вариант длинный №2 (Менее эффективный способ)
index = 0 
while index < len(my_list):
    cur_element = my_list[index]
    if my_list.count(cur_element) > 1:
        my_list.remove(cur_element)
    else:
        index += 1
print(sorted(my_list))