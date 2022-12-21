# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def creat_list(num):
    new_list = []
    for i in range(num):
        k=round(random.uniform(1,10),2)
        new_list.append(k)
    return new_list  

def sum_max_min(n_list):
    alist = []
    for i in range(len(n_list)):
        k=int(n_list[i])
        n=n_list[i]-k
        alist.append(n)
    min1=min(alist)
    max1=max(alist)     
    sum1=round((min1-max1),2)
    return sum1

cl = creat_list(int(input('введите число')))  
print(cl)
sum2 = sum_max_min(cl)
print(sum2)