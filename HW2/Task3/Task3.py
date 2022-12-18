# 3 Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.


def alist(num):
    my_list = list()
    # sum = 0
    for i in range(1, num+1):
        my_list.append(round((1+1/i)**i))
    return my_list

def summ(alist):
    summ = 0
    k=len(alist)
    for i in range(k):
        summ = summ + alist[i]
    return summ

num = int(input('Введите число N: '))
alist1 = alist(num)
print(alist1)
sum1 = summ(alist1)
print(sum1)
