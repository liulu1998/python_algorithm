import numpy as np
from numba import jit, njit


def min_weight_triangulation(n: int, t: np.ndarray, s: np.ndarray, w) -> None:
    for r in range(2, n+1):
        for i in range(1, n-r+2):
            j = i + r - 1
            # print(f"i{i} j{j}")
            t[i][j] = t[i+1][j] + w(i-1, i, j)
            s[i][j] = i
            
            for k in range(i+1, i+r-1):
                u = t[i][k] + t[k+1][j] + w(i-1, k, j)
                if u < t[i][j]:
                    t[i][j] = u
                    s[i][j] = k


def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f"划分的三角形 V{i-1}  V{j}  V{s[i][j]}")


def w(a: int, b: int, c: int) -> int:
    """
    三角形权重函数, 该三角形的边长之和
    """
    global weight
    return weight[a][b] + weight[b][c] + weight[a][c]


if __name__ == "__main__":
    weight = [
        [0,2,2,3,1,4, 0],
        [2,0,1,5,2,3, 0],
        [2,1,0,2,1,4, 0],
        [3,5,2,0,6,2, 0],
        [1,2,1,6,0,1, 0],
        [4,3,4,2,1,0, 0]
    ]

    weight = np.array(weight, dtype=np.int32)
    # print(weight)
    
    t = np.zeros((weight.shape[0]+1, weight.shape[1]+1), dtype=np.int32)
    s = np.zeros((weight.shape[0]+1, weight.shape[1]+1), dtype=np.int8)

    # print(f"weight: {weight.shape}")
    # print(f"t: {t.shape}   s:{s.shape}")

    min_weight_triangulation(weight.shape[0], t, s, w)
    # print(t, s, sep="\n\n")

    traceback(s, 1, weight.shape[0]-1)
