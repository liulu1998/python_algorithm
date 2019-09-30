import numpy as np
from numba import jit, njit
from typing import List


def knapsack(v: List[int], w: List[int], c: int, m: np.ndarray) -> None:
    n = len(v) - 1
    j_max = min(w[n]-1, c)
    for j in range(0, j_max+1):
        m[n][j] = 0
    for j in range(w[n], c+1):
        m[n][j] = v[n]

    for i in range(n-1, 0, -1):
        j_max = min(w[i]-1, c)
        for j in range(0, j_max+1):
            m[i][j] = m[i+1][j]
        for j in range(w[i], c+1):
            m[i][j] = max(m[i+1][j], m[i+1][j-w[i]] + v[i])
    
    m[1][c] = m[2][c]
    if c>= w[1]:
        m[1][c] = max(m[1][c], m[2][c-w[1]] + v[1])


def traceback(m: np.ndarray, w: List[int], c: int, x: List[int]) -> None:
    n = len(w) - 1
    for i in range(0, n):
        if m[i][c] == m[i+1][c]:
            x[i] = 0
        else:
            x[i] = 1
            c -= w[i]
    x[n] = 1 if m[n][c] > 0 else 0


if __name__ == "__main__":
    
    # 物品价值
    v = np.array([8, 3, 2, 11, 6])
    # 物品重量
    w = np.array([4, 2, 2, 5, 7])
    # 背包容量
    c = np.int32(10)

    m = np.zeros((len(v), c+1), dtype=np.int32)
    knapsack(v, w, c, m)

    print(m)
    x = np.zeros((len(v),), dtype=np.int32)
    traceback(m, w, c, x)
    print(x)
