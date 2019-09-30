import numpy as np
from numba import njit
from typing import List


@njit
def lcs_length(x: str, y: str, b: np.ndarray) -> int:
    m = len(x) - 1
    n = len(y) - 1

    c = np.zeros((m+1, n+1), dtype=np.int32)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    return c[m][n]


def lcs(i:int, j: int, x: str, b: np.ndarray) -> None:
    if i == 0 or j == 0:
       return
    
    if b[i][j] == 1:
        lcs(i-1, j-1, x, b)
        print(x[i], end="")

    elif b[i][j] == 2:
        lcs(i-1, j, x, b)
    
    else:
        lcs(i, j-1, x, b)


if __name__ == "__main__":
    x = " abdeijlnrsu"
    y = " dejnuwxyz"

    b = np.zeros((len(x), len(y)), dtype=np.int8)

    # 最长公共子序列长度
    max_len = lcs_length(x, y, b)
    # print(f"最长公共子序列长度:{max_len}")   

    lcs(len(x)-1, len(y)-1, x, b)
    # out: dejnu