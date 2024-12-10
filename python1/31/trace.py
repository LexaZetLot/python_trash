class Wrapper:
    def __init__(self, object):
        self.object = object
    def __getattr__(self, attr):
        print('Trace: ' + attr)
        return getattr(self.object, attr)

x = Wrapper([1, 2, 3])
x.append(4)
print(x.object)

class C1:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)
class C2:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)
class C3(C1, C2):pass
I = C3()
print(I.meth1(), I.metha())
print(I.__dict__)
I.meth2()
I.methb()

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, arg):
        return self.arg + arg
class Product:
    def __init__(self, arg):
        self.arg = arg
    def method(self, arg):
        return self.arg * arg

sobject = Sum(2)
prbject = Product(3)
actions = [square, sobject, prbject.method]

for act in actions:
    print(act(5))

print(actions[-1](5))

class Negate:
    def __init__(self, val):
        self.val = -val
    def __repr__(self):
        return repr(self.val)

actions = [square, sobject, prbject.method, Negate]
for act in actions:
    print(act(5))

print([act(5) for act in actions])