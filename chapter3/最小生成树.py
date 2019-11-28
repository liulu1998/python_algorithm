# -*- encoding: utf-8 -*-
"""
@File    : 最小生成树.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
from typing import List
from copy import deepcopy
from queue import PriorityQueue
from numpy import array, ndarray, inf
import numpy as np


class Edge:
    def __init__(self, u: int, v: int, weight: float):
        """
        Edge类构造器
        :param u: int, 无向边的端点1索引
        :param v: int, 无向边的端点2索引
        :param weight: float, 边的权重
        """
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other) -> bool:
        """小于方法
        """
        return self.weight < other.weight
    
    def __str__(self) -> str:
        return f"{self.u} {self.v} weight:{self.weight}"


class Graph:
    def __init__(self, graph: ndarray):
        """
        Graph类构造器
        :param graph: 2D array, 邻接矩阵表示的无向连通图
        """
        self.graph = graph
        # 结点数
        self.num_node = graph.shape[0]
        # 计算边数
        count = 0
        for i in range(self.num_node):
            for j in range(i + 1, self.num_node):
                if 0 < self.graph[i][j] < inf:
                    count += 1
        self.num_edge = count

    def prim(self) -> List[Edge]:
        """
        Prim 算法, 选点法
        :param graph: 2D array, 邻接矩阵表示的无向连通图
        """
        # 图中节点数
        n = self.num_node
        low_cost = deepcopy(self.graph[0])
        # 最近的邻接节点
        closest = np.zeros((n, ), dtype=np.int32)
        # 记录是否在 S中
        s = np.zeros((n, ), dtype=np.bool)
        s[0] = True
        # 最小生成树
        subgraph = []

        for i in range(n-1):
            min_dist = inf
            j = 0
            for k in range(n):
                if (not s[k]) and low_cost[k] < min_dist:
                    min_dist = low_cost[k]
                    j = k
            s[j] = True
            # closest[i] = j
            subgraph.append(Edge(j, closest[j], self.graph[j][closest[j]]))

            for k in range(1, n):
                if (self.graph[j][k] < low_cost[k]) and (not s[k]):
                    low_cost[k] = self.graph[j][k]
                    closest[k] = j
        return subgraph

    def kruskal(self) -> List[Edge]:
        """
        Kruskal 算法, 选边法
        """
        # 所有边的优先队列, 由小顶堆实现
        edges = PriorityQueue()
        for i in range(self.num_node):
            for j in range(i+1, self.num_node):
                if 0 < self.graph[i][j] < inf:
                    edges.put(Edge(i, j, self.graph[i][j]))
        
        # 记录连通分支, 点i 所属的连通分支为 group[i]
        # 初始每个分支由单个节点构成
        group = [i for i in range(self.num_node)]
        # 记录最小生成树中的边
        subgraph = []

        while not edges.empty() and len(set(group)) > 1:
            edge = edges.get()
            i, j = edge.u, edge.v
            # 若不在同一个连通分支
            if group[i] != group[j]:
                # 合并连通分支
                group = list(map(lambda x: group[i] if x == group[j] else x, group))
                subgraph.append(edge)
        return subgraph

    
if __name__ == "__main__":
    # 无向连通图
    weights = array([
        [0, 6, 1, 5, inf, inf],
        [6, 0, 5, inf, 3, inf],
        [1, 5, 0, 5, 6, 4],
        [5, inf, 5, 0, inf, 2],
        [inf, 3, 6, inf, 0, 6],
        [inf, inf, 4, 2, 6, 0]
    ], dtype=np.float32)

    graph = Graph(weights)

    # Prim 算法得出的最小生成树
    tree = graph.prim() 
    for e in tree:
        print(e)
    print("--------")

    # Kruskal 算法得出的最小生成树
    sub = graph.kruskal()
    for s in sub:
        print(s)
