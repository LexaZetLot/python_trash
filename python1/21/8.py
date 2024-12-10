def f(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')

f(1032132154213515243123)