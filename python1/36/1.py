class MyError(Exception): pass

def oops():
    raise MyError

def oops1():
    try:
        oops()
    except KeyError:
        print('+++++++++')
print(oops1())