# -*- encoding: utf-8 -*-
"""
@File    : 0-1背包_回溯法.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
from typing import List
from copy import deepcopy
from collections import namedtuple


# 物品
Good = namedtuple('Good', ["id", "w", "p", "avg"])


class Knapsack:
    def __init__(self, c: float, w: List[float], p: List[float]):
        """
        0-1背包类构造器
        
        :param c: float, 背包容量
        :param w: List[float], 物品重量
        :param p: List[float], 物品价值
        """
        if len(w) != len(p):
            raise ValueError("价值数组应与重量数组等长")
        self.c = c
        self.goods = [Good._make([pr, i, j, j/i]) for pr, (i, j) in enumerate(zip(w, p))]
        # id用来还原未排序的物品序号, 输出解向量
        self.goods.sort(key=lambda x: x.avg)
        # 物品总数
        self.n = len(self.goods)
        # 背包当前重量
        self.cw = 0.0
        # 背包当前价值
        self.cp = 0.0
        # 背包当前最优价值
        self.bestp = 0.0

        self.bestx = [False] * self.n
        self.x = [False] * self.n
    
    def backtrack(self, i: int):
        """
        回溯法求解 0-1背包问题

        :return List[bool], 解向量, 对应每个物品是否装入
        """
        # 到达叶子结点
        if i > self.n - 1:
           self.bestp = self.cp
           self.bestx = deepcopy(self.x) 
           return
        # 搜索子树
        if self.cw + self.goods[i].w < self.c:
            # 满足可行性约束, 进入左子树
            self.x[self.goods[i].id] = True
            self.cw += self.goods[i].w
            self.cp += self.goods[i].p
            self.backtrack(i+1)
            self.cw -= self.goods[i].w
            self.cp -= self.goods[i].p
        
        if self.bound(i+1) > self.bestp:
            self.x[self.goods[i].id] = False
            # 满足限界函数, 进入右子树
            self.backtrack(i+1)


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


if __name__ == "__main__":
    w = [3, 5, 2, 1]
    p = [9, 10, 7, 4]
    backpack = Knapsack(c=7, w=w, p=p)
    backpack.backtrack(0)
    print(f"{backpack.bestp}\n{backpack.bestx}")
    # out:
    # 20.0
    # [True, False, True, True]
