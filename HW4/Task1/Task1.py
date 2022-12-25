# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import random


def creat_rnd_float(n):
    n = int(n)
    if n < 0:
        print('Вы ввели некорректное число')
        return []
    
    num =round(random.uniform(1,10),n)
    return num

def calc_digit(num, x):
    count = 0
    while x != 1:
        x = x*10
        count += 1
    digit1 = round(num, count)
    return digit1

n = input('введите коэфициент для формирования вещественного числа: ')
c_f = creat_rnd_float(n)
x = float(input('введите число для определения точности: '))
print(calc_digit(c_f, x))