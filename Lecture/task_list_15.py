# Метод copy()
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n') # В данном случае мы вроде как создали копию, но изменения добавились в оба списка. 
# Так происходит, потому что оба элемента ссылаются на один объект.

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy() # В данном случае мы создали копию с отдельной ссылкой. Теперь это два независмых списка.
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')