a = 0; b = 10
while a < b:
    print(a, end=' ')
    a += 1

print()
x = 10
while x:
    x = x - 1
    if x % 2 != 0:
        continue
    print(x, end=' ')

print()
#while True:
#    name = input('Enter your name: ')
#    if name == 'stop': break
#    age = int(input('Enter your age: '))
#    print('Hello', name, '=>', age ** 2)

D = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in D:
    print(key, D[key])

for (k, v) in D.items():
    print(k, v)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

str = 'spam'
str1 = 'scam'
print([x for x in str if x in str1])

print(list(range(5, -5, -1)))

X = 'spam'
for item in X: print(item, end=' ')

print()
for i in range(len(X)): print(X[i], end=' ')


print()
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(list(zip(l1, l2)))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
D2 = {}
for (k, v) in zip(keys, values): D2[k] = v
print(D2)
print(dict(zip(keys, values)))

S = 'spam'
for (offset, item) in enumerate(S):
    print(offset, item)