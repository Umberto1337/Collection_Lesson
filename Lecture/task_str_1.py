#Работа со строками как со списком
text = 'Hello World!'
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')