import numpy as np
from typing import List


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


def lcs(i: int, j: int, x: str, b: np.ndarray) -> None:
    if i == 0 or j == 0:
        return

    if b[i][j] == 1:
        lcs(i-1, j-1, x, b)
        print(x[i-1], end="")

    elif b[i][j] == 2:
        lcs(i-1, j, x, b)
    else:
        lcs(i, j-1, x, b)


if __name__ == "__main__":

    x = "abdfgio"
    y = "acdehijk"

    max_len, b = lcs_length(x, y)

    lcs(len(x), len(y), x, b)
