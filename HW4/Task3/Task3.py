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


# def uniq_elem(alist, num):
#     new_list = []
#     # str_alist =" ".join(map(str, alist))
#     # str_list = str(alist).strip('[]')
#     count = 0
#     k=0
#     for i in range(num):
#         # if str_alist.count(i) == 1:
#         # if alist[i]
#         new_list.append(i)
#         if new_list[i]==alist[i+1]:
           
#     return new_list


x = int(input('введите число a: '))
y = int(input('введите число b: '))
num = int(input('введите число n: '))
# str_alist =" ".join(map(str, alist))
alist = rand_list(x, y, num)
print(alist)
print(set(alist))
# print(" ".join(map(str, alist)))
# print(uniq_elem(rand_list))
