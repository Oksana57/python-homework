# 2 Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def simpl_multipiar(num: int):
    alist = []
    for i in range(2, int(num**0.5+1)):
        k = num % i
        l = int(num/i)
        if k == 0:
            alist.append(i)
            num = l
    return alist

num = int(input('введите натуральное число:'))
print(simpl_multipiar(num))