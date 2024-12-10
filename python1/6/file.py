from ctypes import PyDLL

print(len([1, 2, 3]))
print([1, 2, 3] + [1, 2, 3])
print(['Ni!'] * 4)

print(str([1, 2]) + "34")
print([1, 2] + list("34"))

print(list(map(abs, [1, 2, 3])))

L = [1, 2, 3]
L[1:2] = [4, 5]
print(L)
L[1:1] = [6, 7]
print(L)
L[1:2]=[]
print(L)

table = {'1975': 'Holy Grail',
         '1979': 'Life of Brian',
         '1983': 'The Meaning of Life'}
year = '1983'
movie = table.get(year)
print(movie)
for year in table:
    print(year, table.get(year))

print([title for (title, year) in table.items() if year == '1975'])


print(dict.fromkeys(['a', 'b'], 0))
print(dict(zip(['a', 'b'], [1, 2])))
print({k: v for k, v in zip(['a', 'b'], [1, 2])})
print({x: x ** 2 for x in [1, 2, 3]})
print({c: c * 4 for c in 'SPAM'})
print({c.lower() for c in ['SPAM', 'EGGS', 'HAM']})

print(dict(a=1, b=2, c=3, d=4))