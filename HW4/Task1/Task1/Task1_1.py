# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import decimal 
from  decimal import Decimal, getcontext, ROUND_CEILING

num=Decimal(3.14159265)
y = int(input('введите коэфициент точночти округления числа: '))
x = input('введите число для определенити формата точности: ')
getcontext().prec = y
print(num.quantize(Decimal(x)))