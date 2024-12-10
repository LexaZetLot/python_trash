class FirstCLass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondCLass(FirstCLass):
    def display(self):
        print('Current value = "%s"' % self.data)

class ThirdCLass(SecondCLass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdCLass(self.data + other)
    def __str__(self):
        return '[ThirdCLass: %s]' % self.data
    def __mul__(self, other):
        self.data *= other

class rec():pass

x = FirstCLass()
y = FirstCLass()

x.setdata('King Arthur')
y.setdata(3.14159)

x.display()
y.display()

x.anothername = 'spam'
print(x.anothername)

z = SecondCLass()
z.setdata(42)
z.display()

a = ThirdCLass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()

print(b)

a.__mul__(3)
print(a)

print(list(rec.__dict__.keys()))
print(list(name for name in rec.__dict__ if not name.startswith('__')))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))

print(x.data, x.__dict__['data'])
print(x.__class__)
print(rec.__bases__)

class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs, self.age)
rec1 = Person('King Arthur', 10, 20)
print(list(rec1.info()))