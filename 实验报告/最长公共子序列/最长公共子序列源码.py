# -*- encoding: utf-8 -*-
"""
@File    : 最长公共子序列.py
@Version : 1.0
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
import numpy as np
from typing import List
import random
import time
import string


def lcs_length(x1: str, y1:str) -> (int, np.ndarray):
    # 人为增加一位不同的字符
    x, y = list(x1), list(y1)
    x.insert(0, '+')
    y.insert(0, '-')
    x, y = "".join(x), "".join(y)


    # c[i][j] 为 Xi 和 Yj 的最长公共子序列长度
    c = np.empty((len(x), len(y)), dtype=np.int32)
    # 初始化边界值
    c[0, :] = 0
    c[:, 0] = 0

    # b[i][j] 为 c[i][j] 由哪个子问题的解得到
    b = np.empty((len(x), len(y)), dtype=np.int8)

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                # 情况1, 该位置元素相等
                b[i][j] = 1

            # 取两个子问题中较大的解
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2

            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    return c[len(x)-1][len(y)-1], b


def lcs(i: int, j: int, x: str, b: np.ndarray, result:list) -> None:
    if i == 0 or j == 0:
        return

    if b[i][j] == 1:
        lcs(i-1, j-1, x, b, result)
        result.append(x[i-1])

    elif b[i][j] == 2:
        lcs(i-1, j, x, b, result)
    else:
        lcs(i, j-1, x, b, result)


if __name__ == "__main__":
    x = input("输入第一个字符串\n")
    y = input("输入第二个字符串\n")
    
    max_len, b = lcs_length(x, y)

    result = []
    lcs(len(x), len(y), x, b, result)

    print(''.join(result))
