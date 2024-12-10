from number import Number

class MyNumber(Number):
    def add(self, other):
        print('in Python add...')
        Number.add(self, other)
    def mul(self, other):
        print('in Python mul...')
        self.data = self.data * other

num = MyNumber(1)
num.add(4)
num.display()
num.sub(2)
num.display()
print(num.square())

num.data = 99
print(num.data)
num.display()

num.mul(2)
num.display()
print(num)
del num