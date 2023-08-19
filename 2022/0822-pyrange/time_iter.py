"""Compare hand-written __iter__ vs __len__/__getitem__ fall-back."""
from my_timeit import mintime

from pyrange import pyrange

n = 1_000_000
k = 100

print(f"Iterating over {n} elements.")

pyrange_ = pyrange(n)


def iter_pyrange():
    for _ in pyrange_:
        pass


print(f"pyrange bespoke iter: {mintime(iter_pyrange, k):.2e}")

# del pyrange.__iter__
# pyrange_ = pyrange(n)
# def iter_pyrange_infer():
#     for _ in pyrange_:
#         pass
# print(f"pyrange infer iter: {mintime(iter_pyrange_infer, k):.2e}")

builtin_range = range(n)


def iter_range():
    for _ in builtin_range:
        pass


print(f"pyrange infer iter: {mintime(iter_range, k):.2e}")
