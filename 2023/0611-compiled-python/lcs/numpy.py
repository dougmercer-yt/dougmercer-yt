import numpy as np


def lcs_numpy(a, b):
    dp = np.zeros((len(a) + 1, len(b) + 1), dtype=np.int32)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i, j] = dp[i - 1, j - 1] + 1
            else:
                dp[i, j] = max(dp[i - 1, j], dp[i, j - 1])
    return dp[-1, -1]
