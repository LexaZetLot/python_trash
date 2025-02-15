class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'mrg', pay)
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)

class Department:
    def __init__(self, *name):
        self.members = list(name)
    def addMember(self, person):
        self.members.append(person)
    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100)
    tom = Manager('Tom Jones', 500)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()