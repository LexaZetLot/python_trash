from functools import reduce
from math import factorial


def fact1(x):
    return x * fact1(x - 1) if x > 1 else 1
def fact2(x):
    if x == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, x + 1))
def fact3(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    return fac
print(fact1(6))
print(fact2(6))
print(fact3(6))
print(factorial(1000))