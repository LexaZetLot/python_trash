import struct
import decimal
from fractions import Fraction

L = [123, 'spam', 1.23, 'NI']
print(L)
L.pop(2)
print(L)

M = ['bb', 'aa', 'cc']
print(M)
M.sort()
print(M)
M.reverse()
print(M)

Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Matrix)
print(Matrix[0])

col2 = [row[1] for row in Matrix]
print(col2)
print([row[1] + 1 for row in Matrix])
print([row[1] for row in Matrix if row[1] % 2 == 0])

diag = [Matrix[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c * 2 for c in 'spam']
print(doubles)

print(list(range(4)))
print(list(range(-6, 7, 2)))
print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

G = (sum(row) for row in Matrix)
print(G.__next__())
print(G.__next__())
print(G.__next__())

print(list(map(sum, Matrix)))
print({sum(row) for row in Matrix})
print({i : sum(Matrix[i]) for i in range(3)})

print([ord(x) for x in 'spaam'])
print({ord(x) for x in 'spaam'})
print({x: ord(x) for x in 'spaam'})
print((ord(x) for x in 'spaam'))

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])
D['quantity'] += 1
print(D)

D1 = {}
D1['name'] = 'Bob'
D1['job'] = 'dev'
D1['age'] = 40
print(D1)
print(D1['name'])

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr'], 'age': 40}
print(rec)
print(rec['name'])
print(rec['jobs'])
rec['jobs'].append('janitor')
print(rec['jobs'])

D2 = {'a': 1, 'b': 2, 'c': 3}
print(D2)
D2['e'] = 99
print(D2)
if not 'f' in D2:
    print('missing')

print(D2.get('x', 0))
print(D2['x'] if 'x' in D2 else 0)

Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
print(squares)

T = (1, 2, 3, 4)
print(len(T))
print(T + (5, 6))
print(T[0])
print(T.index(4))
print(T.count(4))
T = (2,) + T[1:]
print(T)

T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])

f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('data.txt', 'r')
text = f.read()
print(text)
print(text.split())

packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('data.bin', 'wb')
file.write(packed)
file.close()

data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>i4sh', data))

S = 'sp\xc4m'
print(S)
print(S[2])
file = open('unidata.txt', 'w', encoding='utf-8')
file.write(S)
file.close()
text = open('unidata.txt', 'r', encoding='utf-8').read()
print(text)
print(len(text))

raw = open('unidata.txt', 'rb').read()
print(raw)
print(len(raw))

print(text.encode('utf-8'))
print(raw.decode('utf-8'))

print(text.encode('latin-1'))
print(text.encode('utf-16'))
print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))

X = set('spam')
Y = {'h', 'a', 'm'}
print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)
print({n ** 2 for n in [1, 2, 3, 4]})

print(list(set([1, 2, 3, 4, 1, 3, 4])))
print(set('spam') - set('ham'))
print(set('ham') == set('spam'))

print('p' in set('spam'), 'p' in set('spam'), 'ham' in ['eggs', 'spam', 'ham'])
print(1 / 3)
print((1 / 2) + (2 / 3))
d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
bob = Worker('bob', 100)
sue = Worker('sue', 200)
print(bob.lastName(), sue.lastName())
print(bob.giveRaise(.10))
print(bob.pay)