import numpy as np
import taichi as ti

ti.init(arch=ti.cpu)


def lcs_taichi_ndarray(a: np.ndarray, b: np.ndarray) -> int:
    dp = ti.ndarray(dtype=ti.i32, shape=(len(a) + 1, len(b) + 1))
    return _compute(a, b, dp)

@ti.kernel
def _compute(a: ti.types.ndarray(), b: ti.types.ndarray(), dp: ti.types.ndarray()) -> int:
    ti.loop_config(serialize=True)
    for i in range(1, a.shape[0] + 1):
        for j in range(1, b.shape[0] + 1):
            if a[i - 1] == b[j - 1]:
                dp[i, j] = dp[i - 1, j - 1] + 1
            else:
                dp[i, j] = ti.max(dp[i - 1, j], dp[i, j - 1])
    return dp[a.shape[0], b.shape[0]]
