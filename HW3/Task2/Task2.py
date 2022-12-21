# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def create_list (len1,num):
    new_list = []
    for i in range(len1):
        new_list.append(random.randint(1,num))
    return new_list    

def composition1(n_list):
    comp_list = []
    if len(n_list)%2==0:
        num=int(len(n_list)/2)
    else:
        num=int(len(n_list)/2+1)   
    for i in range(0, num):
        result = n_list[i]*n_list[len(n_list)-1-i]
        comp_list.append(result)    
    return comp_list       


cl = create_list(int(input('введите длинну массива')),int(input('введите число')))  
print(cl)
comp1 = composition1(cl)
print(comp1)


