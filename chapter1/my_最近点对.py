from math import sqrt
import numpy as np
from typing import List


class Pair(object):
    def __init__(self, p1, p2, dist):
        self.p1 = p1
        self.p2 = p2
        self.dist = dist
    
    def __str__(self):
        return f"-----------\n({self.p1[0]}, {self.p1[1]}) and ({self.p2[0]}, {self.p2[1]})\ndist: {self.dist}"
    
    @staticmethod
    def distance(p1, p2):
        if p1.size == 0 or p2.size == 0:
            return np.float("inf")
        return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


class ClosestPair(object):
    def __init__(self, s: np.ndarray):
        self.s = s
        self.cpair = None

    def cpair(self):
        
def cpair2(s) -> Pair:
    """
    二维最接近点对
    """
    if s.shape[0] == 3:
        d1 = Pair.distance(s[0], s[1])
        d2 = Pair.distance(s[1], s[2])
        d3 = Pair.distance(s[0], s[2])
        if d1 <= d2 and d1 <= d3:
            return Pair(s[0], s[1], d1)
        elif d2 <= d3:
            return Pair(s[1], s[2], d2)
        else:
            return Pair(s[0], s[2], d3)

    if s.shape[0] == 2:
        return Pair(s[0], s[1], Pair.distance(s[0], s[1]))

    if s.shape[0] == 1:
        return Pair(None, None, np.float("inf"))
    
    # 依照 y坐标预排序
    s = s[np.argsort(s[:, 1])]

    # x 坐标中位数
    mid_x = np.median(s[:, 0])
    print(f"mid_x: {mid_x}")
    # 根据 x坐标中位数, 将 S 划分为两半
    s1 = s[s[:, 0] <= mid_x, :]
    s2 = s[s[:, 0]  > mid_x, :]

    # 左, 右部分最短距离
    pair1 = cpair2(s1)
    pair2 = cpair2(s2)
    
    # print(pair1, pair2, sep="\n\n")
    # 最近点对, 最短距离
    best = pair1 if pair1.dist < pair2.dist else pair2
    dm = best.dist

    # print("左右两边最好的:")

    # 左部, 右部 距离分割线 距离小于 dm 的点 
    p1 = s1[abs(s1[:, 0] - mid_x) <= dm, :]
    p2 = s2[abs(s2[:, 0] - mid_x) <= dm, :]
    # 分别根据 y坐标排序
    # p1 = p1[np.argsort(p1[:, 1])]    
    # p2 = p2[np.argsort(p2[:, 1])]

    for point in p1:
        c = p2[ np.sqrt((p2[:, 0] - point[0])**2 + (p2[:, 1] - point[1])**2) < dm, :]
        if c.size == 0:
            continue
        c = c[np.argsort(np.sqrt((c[:, 0] - point[0])**2 + (c[:, 1] - point[1])**2))]
        
        tmp_dist = Pair.distance(c[0], point)
        if tmp_dist < dm:
            best = Pair(point, c[0], tmp_dist)
            dm = tmp_dist

    return best


if __name__ == "__main__":
    S = [
        (0, 1), (3, 2),
        (4, 3), (5, 1),
        (2, 1), (1, 2),
        (6, 2), (7, 2), 
        (8, 3), (4, 5), 
        (9, 0), (6, 4)
    ]

    S = np.array(S, dtype=np.float32)

    pair = cpair2(S)
    print(pair)
    # out:
    # (6.0, 2.0) and (7.0, 2.0)
    # dist: 1.0