def test(reps, func, *args):
    import time
    start = time.time()
    for i in range(reps):
        func(*args)
    return time.time() - start