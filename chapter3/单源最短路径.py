from typing import List
from copy import deepcopy
import numpy as np
from numpy import ndarray, array, inf


def dijkstra(v: int, graph: ndarray) -> (ndarray, ndarray):
    """
    迪杰斯特拉算法, 求单源最短路径

    :param v: int, 源点的索引, 从0开始
    :param graph: 2D array, 邻接矩阵表示的有向图
    :return dist: array, 源点到各点的最短距离
    :return prev: array, 最短路径
    """
    num_node = graph.shape[0]
    # === 初始化 ===
    # 记录节点是否在 S 集合中, 初始S 只有源点
    s = np.zeros((num_node, ), dtype=np.bool)
    s[v] = True

    # 记录源点到各点的特殊路径长度
    dist = deepcopy(graph[v])
    # 记录最短路径
    prev = np.empty((num_node, ), dtype=np.float64)
    for p, d in zip(prev, dist):
        p = -1 if d==inf else v 

    for i in range(num_node):
        temp = inf
        u = v
        for j in range(num_node):
            # 不在S中, 且到该点距离最小
            if not s[j] and dist[j] < temp:
                temp = dist[j]
                u = j
        # 加入S 集合
        s[u] = True

if __name__ == "__main__":
    graph = array([
        [0, 10, inf, 30, 100],
        [inf, 0, 50, inf, inf],
        [inf, inf, 0, inf, 10],
        [inf, inf, 20, 0, 60],
        [inf, inf, inf, inf, 0]
    ], dtype=np.float64)

    dist, prev = dijkstra(0, graph)
    

