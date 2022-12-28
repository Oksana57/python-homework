# 2 Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def simpl_multipiar(num: int):
    alist = []
    # while num>1:
    for i in range(2, int(num+1)):
        k = num % i
        l = int(num/i)
        if k == 0:
            alist.append(i)
            num = l
            if num==1:
                break
    return alist

num = int(input('введите натуральное число:'))
print(simpl_multipiar(num))