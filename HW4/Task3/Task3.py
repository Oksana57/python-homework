#  3 Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random


def rand_list(a, b, n):
    alist = []
    for i in range(n):
        if a < b:
            k = random.randint(a, b)
        else:
            k = random.randint(b, a)
        alist.append(k)
    return alist

def rang_list(alist1):
    new_list=[]

    for i in range(0, len(alist1)):
        for j in range(i+1, len(alist1)):
            if alist1[i]!=alist1[j]:
                count=1
            else:
                count = 0
                break
        if count ==1:         
            new_list.append(alist1[i]) 
    return new_list


x = int(input('введите число a: '))
y = int(input('введите число b: '))
num = int(input('введите число n: '))
alist1 = rand_list(x, y, num)
print(alist1)
r_n = rang_list(alist1)
print(r_n)  


