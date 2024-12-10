def decorator(cls):
    class Wrapper(cls):
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:
    def __init__(self, a, b):
        self.attr = 'spam'

x = C(1, 2)
print(x.attr)


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
    print(a + b + c)
@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)
spam(a=4, b=5, c=6)
eggs(2, 1562)
eggs(4, y=6)



def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):
    print(a + b + c)

@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)
spam(a=4, b=5, c=6)

eggs(2, 16)
eggs(4, y=4)             
