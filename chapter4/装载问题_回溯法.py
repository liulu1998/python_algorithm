# -*- encoding: utf-8 -*-
"""
@File    : 装载问题_回溯法.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
from typing import List
from copy import deepcopy


def backtrack(i: int):
    """
    回溯法求装载问题
    :param i:int, 货物索引 0~n-1
    """
    global n, w, bestw, bestx, r, cw
    # 叶子节点
    if i > n-1:
        if cw > bestw:
            bestw = cw
            bestx = deepcopy(x)
        return
    # 未考察的货物的总重量
    r -= w[i]
    # 可行性约束
    if cw + w[i] <= c:
        x[i] = True
        cw += w[i]
        backtrack(i+1)

        # 准备进入右子树
        cw -= w[i]
    # 限界函数
    if cw + r > bestw:
        x[i] = False
        backtrack(i+1)
    r += w[i]
        

if __name__ == "__main__":
    # 货物重量
    w = [20, 10, 25, 15, 8]
    # 货物总数
    n = len(w)
    # 船1 的载重量
    c = 50
    # 当前载重量
    cw = 0.0
    # 当前最优载重量
    bestw = 0.0
    # 未考察的载重量
    r = sum(w)
    # 最优解向量
    bestx = [False] * n
    # 当前解向量
    x = [False] * n
    
    backtrack(0)
    print(bestx)
