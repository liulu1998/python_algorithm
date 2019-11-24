# -*- encoding: utf-8 -*-
"""
@File    : 0-1背包_动态规划.py
@Version : 1.0
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
import numpy as np
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

    c = int(input("输入背包容量(整型)\n"))
    w = [int(i) for i in input("依次输入物品重量(整型), 空格分隔, 回车结束\n").split()]
    v = [int(i) for i in input("依次输入物品价值(整型), 与重量一一对应, 空格分隔, 回车结束\n").split()]

    m = np.zeros((len(v), c+1), dtype=np.int32)
    knapsack(v, w, c, m)

    # 物品选或不选的向量
    x = np.zeros((len(v),), dtype=np.int32)
    traceback(m, w, c, x)
    print(f"最优解: {x}\n最优值: {sum([a*b for a, b in zip(v, x)])}")
