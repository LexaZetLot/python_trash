#def kaboom(x, y):
#    print(x + y)
#
#
#try:
#    kaboom([1, 2, 3], 'spam')
#except TypeError:
#    print('TypeError')
#print('resuming here')
#
#class MyError(Exception): pass
#
#def stuff(file):
#    raise MyError()
#
#file = open('data', 'w')
#
#try:
#    stuff(file)
#finally:
#    file.close()
#print('done')

#sep = '-' * 45 + '\n'
#
#
#print(sep + 'EXCEPTION RAISED AND CAUGHT')
#try:
#    x = 'spam'[99]
#except IndexError:
#    print('except run')
#finally:
#    print('finally run')
#print('after run')
#
#
#print(sep + 'NO EXCEPTION RAISED')
#try:
#    x = 'spam'[3]
#except IndexError:
#    print('except run')
#finally:
#    print('finally run')
#print('after run')
#
#
#print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
#try:
#    x = 'spam'[3]
#except IndexError:
#    print('except run')
#else:
#    print('else run')
#finally:
#    print('finally run')
#print('after run')
#
#
#print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
#try:
#    x = 1 / 0
#except IndexError:
#    print('except run')
#finally:
#    print('finally run')
#print('after run')

#X = 99
#try:
#    1 / 0
#except Exception as X:
#    print(X)
#

def f(x):
    assert x < 0, 'x must be positive'
    return x ** 2
print(f(1))