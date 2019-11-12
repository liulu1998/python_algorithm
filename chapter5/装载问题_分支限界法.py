# -*- encoding: utf-8 -*-
"""
@File    : 装载问题_分支限界法.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""

from typing import List
from queue import PriorityQueue


class BBNode:
    def __init__(self, parent, is_left: bool):
        """ 子集树结点构造器
        :param parent: BBNode, 该结点的父结点
        :param is_left: bool, 该结点是否为父结点的左孩子
        """
        self.parent = parent
        self.is_left = is_left
    
    def __str__(self):
        return "BBNode "+str(self.is_left)


class QueueNode:
    def __init__(self, node: BBNode, uweight: float, layer: int):
        """ 优先队列结点构造器
        :param node: BBNode, 对应的子集树结点
        :param uweight: 子集树结点对应的上界(限界函数)
        :param layer: int, 子集树结点所在的层序号
        """
        self.node = node
        self.uweight = uweight
        self.layer = layer

    def __lt__(self, other):
        """ 小于方法, 因优先队列由于小顶堆实现, 反转比较结果
        """
        return self.uweight > other.uweight


class MaxLoading:
    def __init__(self, c1: float, weights: List[float]):
        """ 装载问题构造器
        :param c1: float, 第一艘船的最大载重量
        :param weights: List[float], 货物重量数组
        """
        self.c1 = c1
        self.weights = weights
        self.n = len(self.weights)
        self.queue = PriorityQueue(maxsize=2**(self.n + 1))
        self.bestw = 0.0
        self.bestx = [0] * self.n

    def max_loading(self):
        # 当前扩展结点
        e: BBNode = None
        # 扩展结点对应的载重量
        ew = 0.0
        # 未考察的货物的总重量
        r = [0] * self.n
        for j in range(self.n-2, -1, -1):
            r[j] = r[j+1] + self.weights[j+1]

        i = 0
        while i < self.n:
            # 若加入当前货物后的载重量
            temp_w = ew + self.weights[i]

            if temp_w <= self.c1:
                # 左孩子满足约束条件
                self.bestw = temp_w
                left_node = BBNode(parent=e, is_left=True)
                self.queue.put(QueueNode(node=left_node, uweight=temp_w+r[i], layer=i+1))
                # TODO self.c1 变化

            # if ew + r[i] > self.bestw: 
            # 右孩子为可行解
            right_node = BBNode(parent=e, is_left=False)
            self.queue.put(QueueNode(node=right_node, uweight=ew+r[i], layer=i+1))

            queue_node = self.queue.get()
            i = queue_node.layer
            e = queue_node.node
            ew = queue_node.uweight - r[i-1] 

        for j in range(self.n-1, -1, -1):
            self.bestx[j] = 1 if e.is_left else 0
            e = e.parent

        return self.bestx


if __name__ == "__main__":
    # w = [20, 10, 25, 15, 8]
    # c = 50
    c = float(input("输入船1的最大载重量(浮点型), 回车结束\n"))
    w = [float(i) for i in input("依次输入货物货物重量(浮点型), 空格分隔, 回车结束\n").split()]
    load = MaxLoading(c1=c, weights=w)

    result = load.max_loading()
    print(f"result:\n{result}")
    # out
    # [0, 1, 1, 1, 0]
