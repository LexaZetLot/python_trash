L = list(map(lambda x: 2 ** x, range(100)))
if 32 in L:
    print('at index', L.index(32))
else:
    print(32, 'not found')