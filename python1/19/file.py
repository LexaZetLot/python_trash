import operator
import sys
from functools import reduce


def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])
print(mysum([1,2,3,4,5]))

sys.getrecursionlimit()

def echo(message):
    print(message)
echo('Hello World!')
x = echo
x('Hello World!')

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c
print(func(1, 2, 3))
print(func.__annotations__)

f = lambda x, y: x + y
print(f(1, 2))

x = (lambda a="fee", b="fie", c="foe": a + b + c)
print(x())

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action
act = knights()
print(act('robin'))

lower = (lambda x, y: x if x < y else y)
print(lower(1, 2))

showall = lambda x: list(map(sys.stdout.write, x))
showall(['spma', 'tosat', 'eggs\n'])

action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))

co = [1, 2, 3, 4]
print(list(map((lambda x: x + 3), co)))

print(list(filter(lambda x: x % 2 == 0, range(0, 100))))

print(reduce((lambda x, y: x + y), co))
print(reduce(lambda x, y: x * y, co))
print(reduce(operator.add, co))