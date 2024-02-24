'''
Задание №6
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
'''

text = sorted(input('Введите текст: ').split())
max_len = 0
print(text)

for word in text:
    word_len = len(word)
    if max_len < word_len:
        max_len = word_len

for nn, word in enumerate(text, 1):
    print(f'{nn}.{word:>{max_len}}')