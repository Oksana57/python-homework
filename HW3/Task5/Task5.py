# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):
    # alist=[]
    if n <=1:
        return n
    else:
       return fib(n-1)+fib(n-2)
        

def feb_neg(n1):
    if n1 ==-1:
        return 1
    elif n1==-2:
        return -1
    else:
        return fib(-n1)*((-1)**(n1+1))
       

alist1=[]
for e in range(0,9):
    alist1.append(fib(e))
alist2=[]
for e in range(-8,0):
    alist2.append(int(feb_neg(e)))
feb_list = alist2+alist1
print(feb_list)
