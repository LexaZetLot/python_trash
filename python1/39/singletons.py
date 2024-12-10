class singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance


@singleton
class Person:
     def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
     def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val

bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())

X = Spam(val=42)
Y = Spam(99)
print(X.attr, Y.attr)