import time


def mintime(func, n=100):
    times = []
    for _ in range(n):
        t = time.perf_counter()
        func()
        times.append(time.perf_counter() - t)
    return min(times)
