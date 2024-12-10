from traceback import print_exc


class MyError(Exception): pass

def oops():
    raise MyError

def oops1():
    try:
        oops()
    except KeyError:
        print('+++++++++')

def safe(func, *pargs, **kargs):
    try:
        func(*pargs, **kargs)
    except Exception as e:
        from sys import exc_info
        print(exc_info())
        print_exc()

safe(oops)