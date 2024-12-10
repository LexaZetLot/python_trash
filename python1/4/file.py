L1 = [2, 3, 4]
#L2 = L1[:]
L2 = L1
L1[0] = 24
print(L1)
print(L2)

print(L1 == L2)
print(L1 is L2)

X = 42
Y = 42
print(X == Y)
print(Y is X)