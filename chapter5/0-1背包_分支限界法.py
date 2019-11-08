# -*- encoding: utf-8 -*-
"""
@File    : 0-1背包_分支限界法.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
from typing import List
from queue import PriorityQueue


class BBnode:
    def __init__(self, parent, left: bool):
        """
        BBnode 构造方法, BBnode 为状态空间树的结点

        :param parent: BBnode, 该结点的父节点
        :param left: bool, 左儿子标志
        """
        self.parent = parent
        self.left = left


class QueueNode:
    def __init__(self, node: BBnode, weight: float, profit: float, upper: float):
        """
        QueueNode 构造方法, QueueNode为优先队列中的结点

        :param node: BBnode, 对应的状态空间树中的结点
        :param weight: float, node 对应的重量
        :param profit: float, node 对应的价值
        :param upper: node 对应的上界
        """
        self.node = node
        self.weight = weight
        self.profit = profit
        self.upper = upper

    def __lt__(self, other):
        """
        小于方法, 因优先队列由小顶堆实现, 故反转比较结果
        
        :param other: QueueNode
        """
        return self.upper > other.upper


class BBKnapsack:
    def __init__(self, c: float, w: List[float], p: List[float]):
        """
        BBKnapsack 构造方法

        :param c: float, 背包容量
        :param w: List[float], 物品重量数组
        :param p: List[float], 物品价值数组, 元素与w中元素对应
        """
        if len(w) != len(p):
            raise ValueError("重量数组应与价值数组等长")
        self.c = c
        # TODO 物品根据单位价值降序排序
        self.w = w
        self.p = p
        # 物品总数
        self.n = len(w)
        # 当前背包重量
        self.cw = 0.0
        # 当前背包中价值
        self.cp = 0.0
        # 最优解
        self.bestx = [False] * self.n
        # 优先队列
        self.queue = PriorityQueue(maxsize=2**self.n)

    def bound(self, i: int) -> float:
        """
        限界函数, self.goods 需要根据平均价值降序排列好

        :param i: int
        """
        # 背包剩余容量
        cleft = self.c - self.cw
        # 上界
        bound = self.cp
        # 循环结束时的循环变量索引
        final = None

        for index, good in enumerate(self.goods[i: self.n]):
            if good.w > cleft:
                # 在循环外部无法获得 index
                # final 为循环跳出时 遍历到的物品的索引
                final = index + i
                break
            cleft -= good.w
            bound += good.p

        if final:
            # 当作连续背包, 计算上界
            bound += self.goods[final].p * cleft / self.goods[final].w
        return bound
