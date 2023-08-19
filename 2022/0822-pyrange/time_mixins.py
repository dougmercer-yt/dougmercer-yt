"""Compare hand-written count/index vs fall-back."""
import time

from pyrange import pyrange

n = 1_000_000

print(f"Getting index of element {n-1} from {n} elements.")

pyrange_ = pyrange(n)
t = time.perf_counter()
pyrange_.index(n - 1)
print(f"pyrange index: {time.perf_counter() - t:.1e}")

builtin_range = range(n)
t = time.perf_counter()
builtin_range.index(n - 1)
print(f"built-in index: {time.perf_counter() - t:.1e}")

pyrange_ = pyrange(n)
t = time.perf_counter()
pyrange_.count(n - 1)
print(f"pyrange count: {time.perf_counter() - t:.1e}")

builtin_range = range(n)
t = time.perf_counter()
builtin_range.count(n - 1)
print(f"built-in count: {time.perf_counter() - t:.1e}")
