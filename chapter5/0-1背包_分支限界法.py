# -*- encoding: utf-8 -*-
"""
@File    : 0-1背包_分支限界法.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
import math
from typing import List
from queue import PriorityQueue
from collections import namedtuple

# 物品信息 id, 重量, 价值, 单位价值
Good = namedtuple('Good', ["id", "weight", "profit", "avg"])


class BBNode:
    def __init__(self, parent, left: bool):
        """ BBNode 构造方法, BBNode 为状态空间树的结点

        :param parent: BBNode, 该结点的父节点
        :param left: bool, 是否 为父节点的左孩子
        """
        self.parent = parent
        self.left = left


class QueueNode:
    def __init__(self, node: BBNode, weight: float, profit: float, upper: float, lower: float, layer: int):
        """ QueueNode 构造方法, QueueNode为优先队列中的结点

        :param node: BBNode, 对应的状态空间树中的结点
        :param weight: float, node 对应的重量
        :param profit: float, node 对应的价值
        :param upper: node 对应的上界
        :param layer: int, node 所在子集树的层序号
        """
        self.node = node
        self.weight = weight
        self.profit = profit
        self.upper = upper
        self.lower = lower
        self.layer = layer

    def __lt__(self, other):
        """ 小于方法, 因优先队列由小顶堆实现, 故反转比较结果
        
        :param other: QueueNode
        """
        # 上界相等 (浮点数相等)
        if math.isclose(self.upper, other.upper):
            return self.lower > other.lower
        return self.upper > other.upper


class BBKnapsack:
    def __init__(self, c: float, weights: List[float], profits: List[float]):
        """ BBKnapsack 构造方法

        :param c: float, 背包容量
        :param weights: List[float], 物品重量数组
        :param profits: List[float], 物品价值数组, 元素与w中元素对应
        """
        if len(weights) != len(profits):
            raise ValueError("重量数组应与价值数组等长")

        self.c = c
        self.weights = weights
        self.profits = profits

        # 物品 按照单位价值降序排列
        self.goods = [Good._make([i, w, p, p/w]) for i, (w, p) in enumerate(zip(weights, profits))]
        self.goods.sort(key=lambda x: x.avg, reverse=True)

        # 物品总数
        self.n = len(weights)
        # 当前背包重量
        self.cw = 0.0
        # 当前背包中价值
        self.cp = 0.0
        # 最优解
        self.best_x = [0] * self.n
        # 优先队列
        self.queue = PriorityQueue(maxsize=2**(self.n + 1))

    def bound(self, i: int, is_continuous: bool) -> float:
        """ 限界函数, self.goods 需要根据平均价值降序排列好

        :param i: int
        :param is_continuous: bool, 是否当做连续背包问题求解,
            求上界
        """
        # 背包剩余容量
        cleft = self.c - self.cw
        # 上界
        bound = self.cp
        # 循环结束时的循环变量索引
        final = None

        for index, good in enumerate(self.goods[i: self.n]):
            if good.weight > cleft:
                # 在循环外部无法获得 index
                # final 为循环跳出时 遍历到的物品的索引
                final = index + i
                break
            cleft -= good.weight
            bound += good.profit

        if is_continuous and final:
            # 当作连续背包, 计算上界
            bound += self.goods[final].profit * cleft / self.goods[final].weight
        return bound

    def bb_knapsack(self) -> (float, List[bool]):
        """ 分支限界法求解 0-1背包问题

        :return:
        """
        # 扩展结点
        enode = None
        i = 0
        best_profit = 0.0
        # 当前上界
        upper = self.bound(0, is_continuous=True)
        lower = self.bound(0, is_continuous=False)

        # 非叶子结点
        while i < self.n:
            wt = self.cw + self.goods[i].weight
            # 左孩子满足可行性约束
            if wt < self.c:
                pt = self.cp + self.goods[i].profit
                if pt > best_profit:
                    best_profit = pt
                # TODO enode当前为None,
                left_node: BBNode = BBNode(parent=enode, left=True)
                self.queue.put(QueueNode(node=left_node, upper=upper, lower=lower, weight=wt, profit=pt, layer=i+1))

            upper = self.bound(i+1, is_continuous=True)
            if upper >= best_profit:
                # 右子树可能有最优解, 加入优先队列
                # TODO 加入队列的元素
                right_node: BBNode = BBNode(parent=enode, left=False)
                self.queue.put(QueueNode(node=right_node, upper=upper, lower=lower, weight=self.cw, profit=self.cp, layer=i+1))

            new_node: QueueNode = self.queue.get()
            # 当前扩展结点
            enode: BBNode = new_node.node
            self.cw = new_node.weight
            self.cp = new_node.profit
            upper = new_node.upper
            i = new_node.layer

        # 构造最优解
        for j in range(self.n - 1, -1, -1):
            self.best_x[self.goods[j].id] = 1 if enode.left else 0
            enode = enode.parent

        return self.cp, self.best_x


if __name__ == '__main__':
    w = [5, 3, 1, 2]
    p = [10, 9, 4, 7]
    backpack = BBKnapsack(c=7, weights=w, profits=p)
    best_profit, best_x = backpack.bb_knapsack()

    print(f"{best_profit}\n{best_x}")
    # out
    # 20.0
    # [0, 1, 1, 1]
