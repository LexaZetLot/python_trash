print((1, 2) + (3, 4))
print((1, 2) * 5)
T = (1, 2, 3, 4)
print(T[0], T[1:3])

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
print(tmp)
T = tuple(tmp)
print(T)

T = (1, 2, 3, 4)
L = [x + 20 for x in T]
print(L)

bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)
print(bob['name'], bob['age'])
print(bob.values())
print(tuple(bob.values()))
print(list(bob.items()))

myfile = open('myfile.txt', 'w')
myfile.write('Hello World!\n')
myfile.write('goodbye!\n')
myfile.close()
myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
myfile.close()
myfile = open('myfile.txt', 'w')
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
F = open('myfile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()
chars = open('myfile.txt').read()
print(chars)

D = {'a': 1, 'b': 2}
F = open('dataffile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('dataffile.pkl', 'rb')
D = pickle.load(F)
print(D)

name = dict(first='John', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)
import json
s = json.dumps(rec)
print(s)
o = json.loads(s)
print(o)
print(o == rec)

json.dump(rec, fp=open('testjson.json', 'w'), indent=4)
print(open('testjson.json').read())

F = open('data.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)
values = struct.unpack('>i4sh', data)
print(values)