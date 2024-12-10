import sys

import mins

def changer(a, b):
    a = 2
    b[0] = 'spam'
X = 1
L = [1, 2]
changer(X, L)
print(X, L)

def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y
X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X, L)

def f(a, b=2, c=3): print(a, b, c)

f(1, 2, 3)
f(c = 3, b = 2, a = 1)
f(1, c=3, b=2)
f(1)
f(1, 4)
f(1, c=6)

def f1(*args): print(args)
f1(1, 3, 4)

def f2(**args): print(args)
f2(a=2, b=3)

def f3(a, *pargs, **kargs): print(a, pargs, kargs)
f3(1, 2, 3, x=1, y=2)

def func1(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func1(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func1(**args)

func1(1, *(2, 3), **{'d': 4})

def kwonly(a, *b, c): print(a, b, c)
kwonly(1, 2, c=3)
kwonly(1, c=3)

def kwonly1(a, *, b, c): print(a, b, c)
kwonly1(1, b=2, c=3)

def kwonly1(a, *, b = 'spam', c = 'ham'): print(a, b, c)
kwonly1(1, c=3)

def f4(a, *b, c=6, **d): print(a, b, c, d)
f4(1, 2, 3, x=4, y=5)
f4(1, *(2, 3), **dict(x=4, y=5))

print(mins.min1(3, 4, 1, 2))
print(mins.min2('bb', 'aa'))
print(mins.min3([2, 2], [1, 1], [3, 3]))

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res
def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y
print(minmax(lessthan, 4, 23, 5, 6, 1, 7))
print(minmax(grtrthan, 4, 23, 5, 6, 1, 7))

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

def unin(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res
s1, s2, s3 = "spam", "scam", "slam"
print(intersect(s1, s2, s3))
print(unin(s1, s2, s3))

def print3(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
print3(1, 2, 3)

def print4(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
print4(1, 2, 3)

def print5(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    if kwargs: raise TypeError('extra keyword: %s' % kwargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)