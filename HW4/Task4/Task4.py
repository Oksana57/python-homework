

import random


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
    for i in range(0, k+1):
        if alist[i]!=0:
            if len(poly_list)>1:
                poly_list+=' + '
            if i==k:
                poly_list+=str(alist[i])
            elif i==k-1:
                poly_list+=str(alist[i])+'*x'
            else:
                poly_list+=str(alist[i])+'*x**'+str(k-i)
               
    poly_list+=' = 0'    
    return poly_list
    
    
y=int(input('введите степень k: '))  
alist = creat_rnd_list(y)
print(alist)
print(polinomial(y, alist))


with open('file1.txt', 'a', encoding='utf-8') as output:
    output.write(polinomial(y, alist))

# with open ('file1.txt', 'w') as data:
#     data.write('line1\n')