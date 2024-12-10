from Tools.scripts.summarize_stats import emit_table


class Number:
    def __init__(self, value):
        self.value = value
    def __sub__(self, other):
        return Number(self.value - other)
X = Number(3)
Y = X - 2
print(Y.value)


class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

X = Indexer()
print(X[2:4])

class C:
    def __index__(self):
        return 255
X = C()
print(hex(X))
print(bin(X))
print(oct(X))

class StepperIndex:
    def __getitem__(self, index):
        return self.data[index]
X = StepperIndex()
X.data = "Spam"
print(X[1])
for items in X:
    print(items)
print('p' in X)
print([c for c in X])

class Squares:
    def __init__(self, start, stop):
        self.values = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.values == self.stop:
            raise StopIteration
        self.values += 1
        return self.values ** 2

for i in Squares(1, 5):
    print(i, end=' ')
print()

X = Squares(1, 5)
I = iter(X)
print(next(I))

S = 'ace'
for i in S:
    for j in S:
        print(i + j, end=' ')

class SkipObject:
    def __init__(self, wrapper):
        self.wrapper = wrapper
    def __iter__(self):
        return SkipInterator(self.wrapper)

class SkipInterator():
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapper):
            raise StopIteration
        else:
            itme = self.wrapper[self.offset]
            self.offset += 2
            return itme

alpha = 'abcdef'
skipper = SkipObject(alpha)
I = iter(skipper)
print(next(I), next(I), next(I))

for x in skipper:
    for y in skipper:
        print(x + y, end=' ')
print()

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

for i in Squares(1, 5): print(i, end=' ')
print()

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, index):
        print('get[%s]:' % index, end=' ')
        return self.data[index]
    def __iter__(self):
        print('inter=> ', end=' ')
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end=' ')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):
        print('contains:', x, end=' ')
        return x in self.data

X = Iters([1, 2, 3, 4, 5])
print(3 in X)
for i in X:
    print(i, end=' | ')
print()
print([i ** 2 for i in X])
print(list(map(bin, X)))

I = iter(X)
while True:
    try:
        print(next(I), end=' @')
    except StopIteration:
        break

class Empty:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError(item)


X = Empty()
print()
print(X.age)

class Accesscontrol:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value + 10
        else:
            raise AttributeError(key + ' not allowed')

X = Accesscontrol()
X.age = 40
print(X.age)

class PrivateExc(Exception):pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value
class Test1(Privacy):
    privates = ['age']
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

x = Test1()
y = Test2()

x.name = 'Bob'
print(x.name)
y.age =30
print(y.age)

class Adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other
    def __radd__(self, other):
        print('radd', self.data, other)
        return other + self.data

x = Adder(5)
print(x + 2)
print(2 + x)

class Number:
    def __init__(self, value):
        self.value = value
    def __iadd__(self, other):
        self.value += other
        return self

x = Number(5)
x += 1
x += 1
print(x.value)

class Callee:
    def __call__(self, *pargs, **kwargs):
        print('callee', pargs, kwargs)
C = Callee()
C(1, 2, 3)
C(1, 2, 3, x=4, y=5)

class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other
X = C()
print(X > 'ham')
print(X < 'ham')