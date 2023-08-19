"""Compare hand-written __contains__ vs __iter__."""
from my_timeit import mintime

from pyrange import pyrange

n = 1_000_000
print(f"Checking for {n-1} in range({n}) elements.")

k = 100_000

pyrange_ = pyrange(n)


def contains_pyrange():
    n - 1 in pyrange_


print(f"pyrange bespoke contains: {mintime(contains_pyrange, k):.2e}")

k = 100

del pyrange.__contains__
pyrange_ = pyrange(n)


def contains_pyrange_infer():
    n - 1 in pyrange_


print(f"pyrange infer contains: {mintime(contains_pyrange_infer, k):.2e}")

k = 100_000
builtin_range = range(n)


def contains_range():
    n - 1 in builtin_range


print(f"built-in range contains: {mintime(contains_range, k):.2e}")
