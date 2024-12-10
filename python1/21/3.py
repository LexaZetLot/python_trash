def f(*x):
    sum = x[0]
    for y in x[1:]:
        sum += y
    return sum
print(f(1, 2, 4))
print(f('adasd', 'dsasad'))
print(f([1, 2, 3], [3, 4, 5]))