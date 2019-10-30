from copy import deepcopy
import numpy as np
from numpy import array, ndarray, inf


def prim(n: int, graph: ndarray) -> None:
    """
    Prim 算法

    :param n: int, 图中节点数
    :param graph: 2D array, 邻接矩阵表示的无向连通图
    """
    low_cost = deepcopy(graph[0])
    # 最近的邻接节点
    closest = np.zeros((n, ), dtype=np.float32)
    # 记录是否在 S中
    s = np.zeros((n, ), dtype=np.bool)
    s[0] = True
    for i in range(n):
        min_dist = inf
        j = 0
        for k in range(n):
            if (not s[k]) and low_cost[k] < min_dist:
                min_dist = low_cost[k]
                j = k
        s[j] = True
        # closest[i] = j
        print(f"{j}, {closest[j]}")
        for k in range(1, n):
            if graph[i][k] < low_cost[k]:

                


if __name__ == "__main__":
    pass