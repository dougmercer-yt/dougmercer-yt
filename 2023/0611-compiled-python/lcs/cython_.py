# cython: language_level=3, boundscheck=False, wraparound=False
import cython


@cython.locals(i=cython.int, j=cython.int, a=list[cython.int], b=list[cython.int])
def lcs_cython(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(a)][len(b)]
