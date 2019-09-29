from numpy import array, ndarray
from numba import jit, njit
from typing import List

def knapsack(w: List[int], v: List[int], c: float, p: ndarray, head: list[int]) -> float:
    n = len(v) - 1
    head[n+1] = 0
    p[0][0] = 0
    p[0][1] = 0
    left, right, _next = 0, 0, 1
    head[n] = 1
    for i in range(n, 0, -1):
        k = left
        for j in range(left, right+1):
            if p[j][0] + w[i] > c:
                break
            y = p[j][0] + w[i]
            m = p[j][1] + v[i]
        
