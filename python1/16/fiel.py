def times(x, y):
    return x * y
print(times(3, 5))

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

L1 = [1, 2, 5, 7, 9, 231]
L2 = [2, 5, 7, 4, 6]
print(intersect(L1, L2))