import functools
import operator

f = open('text.txt')
print(f.__next__())
print(f.__next__())

L = [1, 2, 3]
I = iter(L)
print(next(I))
print(next(I))
print(next(I))

L = [1, 2, 3]
I = iter(L)
while True:
    try:
        x = next(I)
    except StopIteration:
        break
    print(x)

D = {'a': 1, 'b': 2, 'c': 3}
I = iter(D)
print(next(I))
print(next(I))
print(next(I))

lines = [line.rstrip() for line in open('text.txt') if line[0] == 'p']
print(lines)

print([x + y for x in 'abc' for y in 'lmn'])

print(sorted(open('text.txt')))
print(list(zip(open('text.txt'), open('text.txt'))))
print(list(enumerate(open('text.txt'))))
print(filter(bool, open('text.txt')))
functools.reduce(operator.add, open('text.txt'))

print(set(open('text.txt')))
print({line for line in open('text.txt')})
print({ix: line for ix, line in enumerate(open('text.txt'))})


print(sum([2, 3, 4, 1, 5, 0]))
print(any(['spam', '', 'ni']))
print(all(['spam', '', 'ni']))
print(max([2, 3, 4, 1, 5, 0]))
print(min([2, 3, 4, 1, 5, 0]))


M = map(lambda x: 2 ** x, range(3))
print(list(M))
