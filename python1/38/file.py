class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)


class PropSquare:
    def __init__(self, start):
        self.start = start
    def getX(self):
        return self.start ** 2
    def setX(self, value):
        self.start = value ** 2
    X = property(getX, setX)

P = PropSquare(5)
Q = PropSquare(32)

print(P.X)
P.X = 4
print(P.X)
print(Q.X)


class Person1:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        """name property docs"""
        print('fetch...')
        return self._name
    @name.setter
    def name(self, value):
        print('change...')
        self._name = value
    @name.deleter
    def name(self):
        print('remove...')
        del self._name

bob = Person1('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person1('Sue Jones')
print(sue.name)
print(Person.name.__doc__)

class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')
class Subject:
    attr = Descriptor()

X = Subject()
print(X.attr)
print(Subject.attr)

class D:
    def __get__(*args): print('get')
class C:
    a = D()
X = C()
print(X.a)
print(C.a)
X.a = 99
print(X.a)
print(list(X.__dict__.keys()))
Y = C()
print(Y.a)
print(C.a)

class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')
class C:
    a = D()
X = C()
print(X.a)


class Name:
    """name descriptor docs"""
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name
class Person:
    def __init__(self, name):
        self._name = name
    name = Name()
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)

class DescSquare:
    def __init__(self, start):
        self.start = start
    def __get__(self, instance, owner):
        return self.start ** 2
    def __set__(self, instance, value):
        self.start = value
class Client1:
    X = DescSquare(5)
class Client2:
    X = DescSquare(32)
c1 = Client1()
c2 = Client2()
print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)


class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value

class CalcAttrs:
    X = InstState()
    Y = 3
    def __init__(self):
        self._X = 2
        self.Z  = 4

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
CalcAttrs.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()
print(obj2.X, obj2.Y, obj2.Z)


class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)

x = Person()
x.name
x.name = 'Bob'

class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job
X.pay
X.pay = 99

class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)
X = Wrapper([1, 2, 3])
X.append(4)
print(X.wrapped)


class Person:
    def __init__(self, name):
        self._name = name
    def __getattr__(self, item):
        print('Get: ' + item)
        if item == 'name':
            return self._name
        raise AttributeError(item)
    def __setattr__(self, item, value):
        print('Set: ' + item)
        if item == 'name':
            item = '_name'
        self.__dict__[item] = value
    def __delattr__(self, item):
        print('Delete: ' + item)
        if item == 'name':
            item = '_name'
        del self.__dict__[item]
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)



class CardHolder(object):
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age  = age
        self.addr = addr

    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)

    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)

    def remainGet(self):
        return self.retireage - self.age
    remain = property(remainGet)

def loadclass():
    import sys, importlib
    modulename = sys.argv[1]
    module = importlib.import_module(modulename)
    print('[Using: %s]' % module.CardHolder)
    return module.CardHolder

def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

if __name__ == '__main__':
    CardHolder = loadclass()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age  = 50
    bob.acct = '23-45-67-89'
    printholder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printholder(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')