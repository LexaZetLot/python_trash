import time

def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            alltime = 0
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, alltime)
                print(format % values)
            return result
        return onCall
    return onDecorator

import sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

print('---------------------------------------------------')
# Test on functions

@timer(trace=True, label='[CCC]==>')
def listcomp(N):                             # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]         # listcomp(...) triggers onCall

@timer('[MMM]==>')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))   # list() for 3.X views

for func in (listcomp, mapcall):
    result = func(5)                  # Time for this call, all calls, return value
    func(5000000)
    print(result)


print('---------------------------------------------------')

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @timer()
    def giveRaise(self, percent):            # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)          # tracer remembers giveRaise

    @timer(label='**')
    def lastName(self):                      # lastName = timer(...)(lastName)
        return self.name.split()[-1]         # alltime per class, not instance

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)                           # runs onCall(sue, .10)
print(int(bob.pay), int(sue.pay))
print(bob.lastName(), sue.lastName())        # runs onCall(bob), remembers lastName
