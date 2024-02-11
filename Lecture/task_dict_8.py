# Метод items()
# возвращает объект-итератор dict_items
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for tuple_data in my_dict.items(): #Плохо
    print(tuple_data)
    print(f'{tuple_data[0] = } value befor 100 - {100 - tuple_data[1]}')


for key, value in my_dict.items(): # Хорошо
    print(f'{key = } value befor 100 - {100 - value}')