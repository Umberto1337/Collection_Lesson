# Использование синтаксического сахара "Срезы[::-1]"
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1] # в это случае мы делаем тот же разварот по средством срезов.
print(my_list, new_list, sep='\n')