import numpy as np
from typing import List


def matrix_chain(p: List[int]) -> (np.ndarray, np.ndarray):
    """
    计算M, S

    :param p
        array like, 矩阵对应维数的数组
    :returns m
        ndarray 子问题最优值的矩阵
    :returns s
        ndarray 子问题最优值对应的划分位置k 的矩阵
    """
    # 矩阵数
    n = len(p) - 1  
    # 暂存最优值    
    m = np.zeros((n, n), dtype=np.int32)
    # 最优值的划分位置
    s = np.zeros((n, n), dtype=np.int8)

    # col from 2 to (n-1)
    for col in range(1, n):
        # row from (col-1) to 0
        # TODO 计算顺序有误?
        for row in range(col-1, -1, -1):
            m[row][col] = m[row-1][col] + p[row]*p[col]*p[col+1]
            s[row][col] = row
            # 计算划分最优位置 k
            for k in range(row+1, col):
                tmp_m = m[row][k] + m[k+1][col] + p[row]*p[k+1]*p[col+1]
                # 如果出现更优的划分位置 k
                if tmp_m < m[row][col]:
                    s[row][col] = k
                    m[row][col] = tmp_m
    return m, s

def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    count += p[i]*p[s[i][j]+1]*p[j+1]
    print(f"Multiply A[{i+1}: {s[i][j]+1}] and A[{s[i][j]+2}: {j+1}]")


if __name__ == "__main__":
    # p = np.array([20, 35, 15, 5, 10, 20, 25], dtype=np.int32)
    p = np.array([30, 35, 15, 5, 10, 20, 25], dtype=np.int32)
    
    m, s = matrix_chain(p)

    traceback(s, 0, len(p)-2)
    print(m, s, sep="\n\n")

    # print(f"count:{count}")
