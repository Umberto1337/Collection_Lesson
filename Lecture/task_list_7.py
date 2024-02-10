# Метод index()
# Индекс первого вхождения элемента
my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.index(4) # Ищет элемент со значением 4(не по индеку), а само значение но выводит его индекс.
print(spam, my_list)
eggs = my_list.index(4, spam +1, 90) # здесь также ищет цифру 4, в диопазоне списка 90(символов), со второго элемента индекса.
print(eggs, my_list)
err = my_list.index(3) # ValueError: 3 is not in list