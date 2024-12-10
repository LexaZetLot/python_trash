import timeit

import timer


# print(timer(pow, 2, 1000))
# print(timer(str.upper, 'spam'))
#
# print(total(10000, pow, 1, 1000)[0])
# print(total(10000, str.upper, 'spam'))
# print(bestof(10000, str.upper, 'spam'))
# print(bestof(10000, pow, 1, 1000)[0])
# print(bestof(10000, total, 1000, str.upper, 'spam'))
# print(bestoftotal(50, 10000, str.upper, 'spam'))

resp = 10000
resplist = list(range(resp))

def F(x): return x

def forLoop():
    res = []
    for x in resplist:
        res.append(F(x))
    return res

def listComp():
    return [F(x) for x in resplist]

def mapCall():
    return list(map(F, resplist))

def genExpr():
    return list(F(x) for x in resplist)

def genFunc():
    def gen():
        for x in resplist:
            yield F(x)
    return list(gen())

print('########################################################')
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))


print(min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5)))