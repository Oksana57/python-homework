# 2 Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def simpl_multipiar(num: int):
    alist = []
    n=2
    while num>1:
        if num%n==0:
            alist.append(n)
            num/=n 
        else:
            n+=1
    return alist

   
num = int(input('введите натуральное число:'))
print(simpl_multipiar(num))
