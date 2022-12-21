# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def trans_binary(num):
    new_str=''
    while num >0:
        new_str=new_str+str(num%2)
        num=num//2
    str_bin=new_str[::-1]
    return str_bin

tb=trans_binary(int(input('введите число')))
print(tb)
