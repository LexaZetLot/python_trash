import time, sys
timer =  time.time

def total(reps, func, *pargs, **kargs):
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    return bestof(reps1, total, reps2, func, *pargs, **kargs)