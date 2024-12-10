res = []
for x in 'spam':
    res.append(ord(x))
print(res)

print(list(map(ord, 'spam')))

print([ord(x) for x in 'spam'])

print(list(map((lambda x: x ** 2), range(10))))

print([x for x in range(10) if x % 2 == 0])
print(list(filter(lambda x: x % 2 == 0, range(10))))

print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

print([x + y for x in 'spam' if x in 'sm' for y in 'spam' if y in ('p', 'a')])

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]
print([row[1] for row in M])
print([M[row][1] for row in (0, 1, 2)])
print([M[i][i] for i in range(len(M))])
print([M[i][len(M) - 1 - i] for i in range(len(M))])
print([[col + 10 for col in row] for row in M])
print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])

def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i)

x = gensquares(3)
print(next(x))
print(next(x))
print(next(x))

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print(tuple(ups('aaa,bbb,ccc')))
print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})

def gen():
    for i in range(10):
        X = yield i
    print(X)

G = gen()
print(next(G))
print(G.send(10))
print(G.send(88))
print(next(G))

G = (x ** 2 for x in range(4))
print(iter(G) is G)
print(next(G))
print(next(G))
print(next(G))

for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num / 2))

line = 'aa bb c'
print(''.join(x.upper() for x in line.split() if len(x) > 1))
print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

G = (c * 4 for c in 'abc')
print(list(G))
def timesfour(S):
    for c in S:
        yield c * 4
G = timesfour('abc')
print(list(G))

line = 'aa bbb c'
print(''.join(x.upper() for x in line.split() if len(x) > 1))
def gensub(line):
    for x in line.split():
        if len(x) > 1:
            yield x.upper()
print(''.join(gensub(line)))

L, S = [1, 2, 3], 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

print()
for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L, end=' ')

print()
def scrambler(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res
print(scrambler(['spam', 'pams', 'mspa', 'amsp']))

def scrambler1(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]
print(scrambler1(['spam', 'pams', 'mspa', 'amsp']))

def scrambler2(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq
def scrambler3(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]
print(list(scrambler3(['spam', 'pams', 'mspa', 'amsp'])))
print(list(scrambler2(['spam', 'pams', 'mspa', 'amsp'])))
F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

def mymap(func, *args):
    return [func (*args) for args in zip(*args)]
print(mymap(abs, range(-10, 10,)))

def myap(func, *args):
    return (func (*args) for args in zip(*args))
print(mymap(abs, range(-10, 10,)))

def myzip(*args):
    seqs = [list(S) for S in args]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res
def mymapPad(*args, pad=None):
    seqs = [list(S) for S in args]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res
S1, S2 = 'abs', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S2, S1, pad=99))

def myzip2(*args):
    arg = [list(S) for S in args]
    while all(arg):
        yield tuple(arg.pop(0) for S in arg)
def mymapPad2(*args, pad=None):
    arg = [list(S) for S in args]
    while any(arg):
        yield tuple(arg.pop(0 if S else pad) for S in arg)
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S2, S1, pad=99))

def myzip3(*args):
    minlen = min(len(S) for S in args)
    return [tuple(S[i] for S in args) for i in range(minlen)]
def mymapPad3(*args, pad=None):
    maxlen = max(len(S) for S in args)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in args) for i in index]
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S2, S1, pad=99))