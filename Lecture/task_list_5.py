# Метод pop()
# Удаление элемента по индексу
my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop() # Удаляет последний элемент списка.
print(spam, my_list)
eggs = my_list.pop(1) # удаляет элемент по индексу.
print(eggs, my_list)
err = my_list.pop(10) # IndexError выход за рамки списка по индексу.