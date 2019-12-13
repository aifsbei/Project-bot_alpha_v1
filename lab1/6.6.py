#from cmath import pi
from fractions import Fraction
from math import pow
summ = 0
pi = 3.141592653589793
quantity = int(input())
for i in range(1, quantity + 1):
    summ += Fraction(1, i ** 2)
print("%.15f" % (pi ** 2 / summ))