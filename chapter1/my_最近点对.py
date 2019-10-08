from math import sqrt
import numpy as np
from typing import List


class Pair(object):
    def __init__(self, p1, p2, dist):
        self.p1 = p1
        self.p2 = p2
        self.dist = dist
    
    @staticmethod
    def dist(p1, p2):
        return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def cpair2(s) -> (Pair, float):
    """
    二维最接近点对
    """
    if len(s) == 2:
        return s, Pair.dist(s[0], s[1])
    elif len(s) < 2:
        return s, float("inf")

    # 依照 y坐标预排序
    s = s[np.argsort(s[:, 1])]

    # x 坐标中位数
    mid_x = (min(s[:, 0]) + max(s[:, 0])) / 2
    # 根据 x坐标中位数, 将 S 划分为两半
    s1 = s[s[:, 0] <= mid_x, :]
    s2 = s[s[:, 0]  > mid_x, :]

    # 左, 右部分最短距离
    pair1, d1 = cpair2(s1)
    pair2, d2 = cpair2(s2)

    dm = min(d1, d2)

    # 左部, 右部 距离分割线 距离小于 dm 的点 
    p1 = s1[abs(s1[:, 0]) <= dm, :]
    p2 = s2[abs(s2[:, 0]) <= dm, :]
    # 分别根据 y坐标排序
    # p1 = p1[np.argsort(p1[:, 1])]    
    # p2 = p2[np.argsort(p2[:, 1])]

    for point in p1:
        c = p2[Pair.dist(p2, point) < dm]
        c = c[np.argsort(Pair.dist(c, point))]


        





if __name__ == "__main__":
    S = [
        [1, 3],
        [5, 8], 
        [2, 100],
        [4, 10]
    ]

    S = np.array(S, dtype=np.float32)
