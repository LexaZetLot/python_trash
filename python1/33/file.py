def fetcher(obj, index):
    return obj[index]

try:
    fetcher('spam', 4)
except IndexError:
    print('IndexError')

try:
    raise IndexError
except IndexError:
    print('IndexError')

class AlreadyGotOne(Exception): pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print('AlreadyGotOne')

def after():
    try:
        fetcher('spam', 3)
    finally:
        print('After')
    print('After')

after()