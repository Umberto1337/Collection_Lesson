# Функция sorted()
# my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
# my_list.sort() # TypeError питон не понимает как сравнить сроки и числа между собой.
# res = sorted(my_list) # TypeError аналогично, может работать тока цифрами или строчными. 

# Работа с однотипными данными.
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list) # Сортирует список по порядку
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True) # Сортирует список по порядку и Метод reverse() - разварачивает список.
print(my_list, rev_list, sep='\n')
