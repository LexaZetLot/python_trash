import builtins
import thismod

print(builtins.zip)

X = 100
def func():
    global X
    X -= 1
func()
print(X)


y, z = 1, 2
def all_global():
    global x
    x = y + z
all_global()
print(x)

print(thismod.var)
print(thismod.local(), thismod.glob1(), thismod.glob2(), thismod.glob3())
print(thismod.var)

def f1():
    X = 88
    def f2():
        print(X)
    return f2
action = f1()
action()

def marker(N):
    def action(X):
        return X ** N
    return action
f = marker(3)
print(f(1))

def maker(N):
    return lambda X: X ** N
h = maker(3)
print(h(5))
def makeAction():
    axtc = []
    for i in range(10):
        axtc.append(lambda x, i=i: i ** x)
    return axtc
acrs = makeAction()
print(acrs[3](2))

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += label
    return nested

f = tester(1)
print(f('spam'))

