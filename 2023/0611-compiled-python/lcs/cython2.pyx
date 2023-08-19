# distutils: language=c++
# cython: language_level=3
from cython cimport boundscheck, wraparound
from cython.view cimport array as cvarray
from libc.stdint cimport int32_t


@boundscheck(False)
@wraparound(False)
cpdef int lcs_cython_cpdef(int[:] a, int[:] b):
    cdef int n = len(a)
    cdef int m = len(b)
    cdef int i, j
    cdef int[:, :] dp = cvarray(shape=(n + 1, m + 1), itemsize=sizeof(int), format="i")

    for i in range(n + 1):
        for j in range(m + 1):
            dp[i, j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i] == b[j]:
                dp[i, j] = dp[i - 1, j - 1] + 1
            else:
                dp[i, j] = max(dp[i - 1, j], dp[i, j - 1])

    return dp[n, m]
