import numpy as np
from typing import List
# import matplotlib.pyplot as plt


# 平面点对
class Pair(object):
    def __init__(self, p1, p2, dist=None):
        """
        :param p1, 点1 例如 [1, 2]
        :param p2, 点2 例如 [3, 4.5]
        :param dist, float, 两点距离 不传入则自动计算
        """
        self.p1 = p1
        self.p2 = p2
        self.dist = dist if dist else self.distance(p1, p2)

    @staticmethod
    def distance(a, b) -> float:
        """
        计算两点的欧氏距离
        
        :param a: array, 点1, 例如 [2, 3]
        :param b: array, 点2, 例如 [3.3, 5]
        :return float, 两点的欧氏距离
        """
        return np.sqrt( (a[0]-b[0])**2 + (a[1] - b[1])**2 )

    def __lt__(self, other):
        return self.dist < other.dist
    
    def __str__(self):
        return f"\n({self.p1[0]}, {self.p1[1]}) and ({self.p2[0]}, {self.p2[1]})\ndist: {self.dist}"
    

def cpair2(x: np.ndarray) -> Pair:
    """
    二维最近点对

    :param x
        2D array, 平面中的点, 表示为二维数组
    :return Pair 
    """

    # 三点的情况
    if x.shape[0] == 3:
            d1 = Pair.distance(x[0], x[1])
            d2 = Pair.distance(x[1], x[2])
            d3 = Pair.distance(x[0], x[2])
            if d1 <= d2 and d1 <= d3:
                return Pair(x[0], x[1], d1)
            elif d2 <= d3:
                return Pair(x[1], x[2], d2)
            else:
                return Pair(x[0], x[2], d3)
    # 两点的情况
    if x.shape[0] == 2:
        return Pair(x[0], x[1])
    # 仅有一点
    # if x.shape[0] == 1:
    #     return Pair(None, None, np.float("inf"))

    # 依 x坐标排序
    x = x[np.argsort(x[:, 0])]
    # 依 y坐标排序 (x的副本)
    y = x[np.argsort(x[:, 1])]

    # x 坐标中位数点的索引
    mid = x.shape[0] // 2

    # 左, 右部分最近点对
    pair1: Pair = cpair2(x[0: mid])
    pair2: Pair = cpair2(x[mid: x.shape[0]])

    best = pair1 if pair1 < pair2 else pair2

    # d矩形条内的点
    z = y[abs(y[:, 0] - x[mid][0]) < best.dist]

    for i in range(z.shape[0]):
         for j in range(i+1, z.shape[0]):
             # y 坐标距离小于 d 的才可能欧氏距离小于d
             if z[j][1] - z[i][1] < best.dist:
                 dp = Pair.distance(z[i], z[j])
                 if dp < best.dist:
                     best = Pair(z[i], z[j], dp)
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


    # ==== 绘制散点图 ====
    # plt.scatter(S[:, 0], S[:, 1])
    # plt.title("Points")
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.savefig("points.png")
