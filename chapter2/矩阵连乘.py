# -*- encoding: utf-8 -*-
"""
@File    : 矩阵连乘.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
import numpy as np
from typing import List
import time
import matplotlib.pyplot as plt

def matrix_chain(p: List[int]) -> (np.ndarray, np.ndarray):
    """
    计算M, S

    :param p
        array like, 矩阵对应维数的数组
    :returns m
        ndarray 子问题最优值的矩阵, 二维数组
    :returns s
        ndarray 子问题最优值对应的划分位置k 的矩阵, 二维数组
    """
    # 矩阵数
    n = len(p) - 1  
    # 暂存最优值    
    m = np.empty((n, n), dtype=np.int32)
    for i in range(0, n):
        m[i][i] = 0
    
    # 最优值的划分位置
    s = np.empty((n, n), dtype=np.int8)

    for col in range(1, n):
        for row in range(0, n-col):
            # 沿着斜线自左上向右下计算
            # 当前列数  
            cur_col = row + col
            
            m[row][cur_col] = m[row+1][cur_col] + (p[row] * p[row+1] * p[cur_col+1])
            s[row][cur_col] = row

            # 计算划分最优位置 k
            for k in range(row+1, cur_col):
                tmp_m = m[row][k] + m[k+1][cur_col] + p[row]*p[k+1]*p[cur_col+1]
                # 如果出现更优的划分位置 k
                if tmp_m < m[row][cur_col]:
                    s[row][cur_col] = k
                    m[row][cur_col] = tmp_m
    return m, s


def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f"Multiply A[{i+1}: {s[i][j]+1}] and A[{s[i][j]+2}: {j+1}]")


if __name__ == "__main__":
    # p = [int(i) for i in input("依次输入矩阵维数(整型), 空格分隔, 回车结束\n").split()]
    # p = np.array(p, dtype=np.int32)

    p = np.array([30, 35, 15, 5, 10, 20, 25], dtype=np.int32)
    # 自底向上地计算最优值
    m, s = matrix_chain(p)
    # 构造最优解
    traceback(s, 0, len(p)-2)

    # out:
    # Multiply A[2: 2] and A[3: 3]
    # Multiply A[1: 1] and A[2: 3]
    # Multiply A[4: 4] and A[5: 5]
    # Multiply A[4: 5] and A[6: 6]
    # Multiply A[1: 3] and A[4: 6]
