def f(x):
    if x == 0:
        print('stop')
        return
    print(x)
    f(x - 1)
f(5)