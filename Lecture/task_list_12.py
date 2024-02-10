# Возможности разворотов. Функция Reversed()
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list) 
print(type(res), res) # <class 'list_reverseiterator'> <list_reverseiterator object at 0x00000291389CAB30>

rev_list = list(reversed(my_list)) #Способ развернет список справа на лево.
print(rev_list)

for item in reversed(my_list):
    print(item)