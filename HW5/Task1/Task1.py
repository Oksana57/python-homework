# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str1='Абвгдейка это учеба и абв'
str1=str1.split()
f=lambda elem: 'абв' not in elem.lower()
str2=''
str2=' '.join(list(filter(f, str1)))
print(str1)
print(str2)