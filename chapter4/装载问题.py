# @Author : LIU Lu
# @File : 装载问题.py
# @Date : 2019.10.31

from typing import List
from copy import deepcopy
# # 货物总数
# n = 0
# # 货物重量数组
# w = []
# # 船1的最大载重量
# c = 0.0
# # 当前搜索的解向量
# x = []
# 未考察的货物的总重量
# r = sum(w)
# 当前轮船载重量
# cw = 0.0
# 当前最优载重量
# bestw = 0.0
# 最优解向量
# bestx = []


def backtrack(i: int):
    """
    回溯法
    :param i:int, 货物索引 0~n-1
    n: int, 
    """
    global n, w, bestw, bestx, r, cw
    # 叶子节点
    if i > n-1:
        if cw > bestw:
            bestw = cw
            bestx = deepcopy(x)
        return
    r -= w[i]
    # 可行性约束
    if cw + w[i] <= c:
        x[i] = True
        cw += w[i]
        backtrack(i+1)

        # TODO 正确与否？
        x[i] = False
        cw -= w[i]
    # 限界函数
    if cw + r > bestw:
        x[i] = False
        backtrack(i+1)
    r += w[i]
        

if __name__ == "__main__":
    w = [20, 10, 25, 15, 8]
    n = len(w)
    c = 50
    cw = 0.0
    bestw = 0.0
    r = sum(w)
    bestx = [False] * n
    x = [False] * n
    
    backtrack(0)
    print(bestx)
