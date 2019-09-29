import numpy as np
from numba import jit
from typing import List

@jit
def matrix_chain(p: np.ndarray, m: np.ndarray, s: np.ndarray)->None:
    """
    自下而上计算矩阵连乘积的最优值 m[i][j] 和分裂的位置 s[i][j]

    :param p: ndarray, 矩阵维数的数组
    :param m: ndarray, 保存最优值的矩阵
    :param s: ndarray, 保存最优值对应的分裂位置k的矩阵
    """

    n = len(p) - 1
    for r in range(2, n+1):
        for i in range(1, n-r+2):
            j = i + r -1
            m[i][j] = m[i+1][j] + p[i-1]*p[i]*p[j]
            s[i][j] = i
            for k in range(i+1, j):
                t = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f'Multiply A[{i},{s[i][j]}] and A[{s[i][j]+1},{j}]')


if __name__ == "__main__":
    
    # 矩阵维数
    p = [30, 35, 15, 5, 10, 20, 25]
    p = np.array(p, dtype='int32')
    
    # m[i][j] 记录了 A[i:j] 的最优值
    m = np.zeros((p.shape[0], p.shape[0]), dtype='int32')
    # s[i][j] 记录了 m[i][j] 对应的分裂位置 k
    s = np.zeros((p.shape[0], p.shape[0]), dtype='int32')
    
    matrix_chain(p, m, s)
    traceback(s, 1, p.shape[0] - 1)
