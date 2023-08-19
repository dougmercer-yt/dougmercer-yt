import time

import numpy as np
import typer

app = typer.Typer()


@app.command()
def benchmark(
    n: int = 1000,
    numba: bool = False,
    numpy: bool = False,
    python: bool = False,
    taichi: bool = False,
    mypyc: bool = False,
    cython: bool = False,
    cython_py: bool = False,
    n_reps: int = 1,
):
    funcs = []
    if python:
        import lcs.python
        funcs.append(lcs.python.lcs_python)
    if numpy:
        import lcs.numpy
        funcs.append(lcs.numpy.lcs_numpy)
    if cython_py:
        import lcs.cython_
        funcs.append(lcs.cython_.lcs_cython)
    if cython:
        import lcs.cython2
        funcs.append(lcs.cython2.lcs_cython_cpdef)
    if numba:
        import lcs.numba
        funcs.append(lcs.numba.lcs_numba)
    if mypyc:
        import lcs.mypyc_
        funcs.append(lcs.mypyc_.lcs_mypyc)
    if taichi:
        import lcs.taichi
        import lcs.taichi_field
        funcs.append(lcs.taichi.lcs_taichi_ndarray)
        funcs.append(lcs.taichi_field.lcs_taichi_field_once)
    for f in funcs:
        _benchmark(f, n, n_reps)


def _benchmark(f, n, n_reps):
    rng = np.random.default_rng(12345)
    total_time = 0
    for _ in range(n_reps):
        a = rng.integers(0, 100, n, dtype=np.int32)
        b = rng.integers(0, 100, n, dtype=np.int32)
        if f.__name__ in {"lcs_mypyc", "lcs_cython"}:
            a_ = a.tolist()
            b_ = b.tolist()
        else:
            a_ = a
            b_ = b
        t0 = time.perf_counter()
        val = f(a_, b_)
        t1 = time.perf_counter()
        total_time += t1 - t0
    # from lcs.taichi import ti
    # ti.profiler.print_scoped_profiler_info()

    print(f"Time using {f.__name__}: {total_time}s (answer={val})")


if __name__ == "__main__":
    app()
