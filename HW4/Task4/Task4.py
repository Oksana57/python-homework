

import random
from random import choice

def creat_rnd_list(k):
    n = int(k+1)
    alist=[]
    if n < 1:
        print('Вы ввели некорректное число')
        return []
    for i in range(0,n):
        num = random.randint(0,10)
        alist.append(num)
    return alist



def polinomial(k, alist):
    poly_list=''
    for i in range(k, 0, -1):
        value = choice(alist)
        if value:
            poly_list+=f"{value} *x^{i} {choice('+')}"
        
    return poly_list
    
    
y=int(input('введите степень k: '))  
alist = creat_rnd_list(y)

with open('poly1.txt', 'w', encoding='utf-8') as output:
    output.write(f"{polinomial(y, alist)}{choice(alist)}=0\n")

