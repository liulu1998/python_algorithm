# -*- encoding: utf-8 -*-
"""
@File    : 矩阵连乘.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm

区间 DP
一般的方式:
    - 枚举区间长度
        - 枚举左端点
"""

# import time
from typing import List
import numpy as np
# import matplotlib.pyplot as plt


def matrix_chain(p: List[int]) -> (np.ndarray, np.ndarray):
    """
    计算M, S

    :param p, array like, 矩阵对应维数的数组
    :returns m, ndarray 子问题最优值的矩阵, 二维数组
    :returns s, ndarray 子问题最优值对应的划分位置k 的矩阵, 二维数组
    """
    # 矩阵数
    n = len(p) - 1

    # dp 数组
    dp = np.empty((n, n), dtype=np.int32)
    # 初始化 dp 数组
    dp[:] = 1e9
    for i in range(0, n):
        dp[i][i] = 0

    # 最优值的划分位置
    s = np.empty((n, n), dtype=np.int8)

    for length in range(2, n + 1):      # 枚举区间长度
        for i in range(0, n-1):        # 枚举左端点
            r = i + length - 1        # 计算右端点
            if r > n - 1:   # 右端点越界
                break
            for k in range(i, r):     # 枚举划分位置
                tmp_v = dp[i][k] + dp[k + 1][r] + p[i] * p[k + 1] * p[r + 1]
                if tmp_v < dp[i][r]:
                    dp[i][r] = tmp_v
                    s[i][r] = k
    return dp, s


def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f"Multiply A[{i+1}: {s[i][j]+1}] and A[{s[i][j]+2}: {j+1}]")


if __name__ == "__main__":
    p = np.array([30, 35, 15, 5, 10, 20, 25], dtype=np.int32)
    # 自底向上地计算最优值
    m, s = matrix_chain(p)

    print(f"min cost: {m[0][len(p) - 2]}")
    # 构造最优解
    traceback(s, 0, len(p)-2)

    # out:
    # Multiply A[2: 2] and A[3: 3]
    # Multiply A[1: 1] and A[2: 3]
    # Multiply A[4: 4] and A[5: 5]
    # Multiply A[4: 5] and A[6: 6]
    # Multiply A[1: 3] and A[4: 6]
