# Метод extend()
# Добавление нескольких элементов в конец
a = 42
b = 'Hello World!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.extend(a) # тут выдает ошибку, т.к, он не добавляет по одному элементу.
print(my_list)
my_list.extend(b) # Тут добавит строку последовательно разделенную по буквам и элементам.
print(my_list)
my_list.extend(c) # Здесь сработает и добавит последовательно каждую цифру.
print(my_list)