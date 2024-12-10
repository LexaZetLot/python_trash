from time import perf_counter


class SharedData:
    spam = 42

x = SharedData()
y = SharedData()

print((x.spam, y.spam))

SharedData.spam = 99
print((x.spam, y.spam))

class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)

x = NextClass()
x.printer("Hello")
print(x.message)

NextClass.printer(x, "Hello")
print(x.message)

class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    def method(self):
        print('in Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()





from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

class Sub(Super):
    def action(self): print('in Sub.action')

X = Sub()
X.delegate()

def classtree(cls, indent):
    print('.' * indent, cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)
def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instancetree(B())
    instancetree(F())
selftest()