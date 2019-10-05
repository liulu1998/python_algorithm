from math import sqrt
import numpy as np
from typing import List
import matplotlib.pyplot as plt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} y:{self.y}"

class Point1(Point):
    """
        依 x坐标排序的点
    """
    def __init__(self, x, y, id):
        super().__init__(x, y)
        self.id = id

    def __str__(self):
        return super().__str__()+f" id:{self.id}"

    # 小于方法
    def __lt__(self, other):
        return self.x < other.x
    
    # 等于方法
    def __eq__(self, other):
        return self.x == other.x

class Point2(Point):
    """
        依 y坐标排序的点
    """
    def __init__(self, x, y, p):
        super().__init__(x, y)
        self.p = p

    def __str__(self):
        return super().__str__()+f" p:{self.p}"

    def __lt__(self, other):
        return self.y < other.y

    def __eq__(self, other):
        return self.y == other.y
 
class Pair(object):
    """
        输出的平面点对
    """
    def __init__(self, a: Point1, b: Point1, dist: float):
        self.a = a
        self.b = b
        self.dist = dist

    def __str__(self):
        return self.a.__str__() + self.b.__str__()


def dist(u: Point, v: Point) -> float:
    """
    计算两点欧式距离

    :param u: Point, 点1
    :param v: Point, 点2
    :return float, 两点欧氏距离
    """
    x = u.x - v.x
    y = u.y - v.y
    return sqrt(x**2 + y**2)


def cpair2(x: List[Point1]) -> Pair:
    """
    二维平面的最接近点对
    """
    if len(x) < 2:
        return None

    # 依 x坐标排序, in-place 操作
    x.sort()
    y = [ Point2(p.x, p.y, i) for (i, p) in enumerate(x) ]
    # 依 y坐标排序, in-place 操作
    y.sort()
    z = list(range(len(x)))
    return closest_pair(x, y, z, 0, len(x)-1)


def closest_pair(x: List[Point1], y: List[Point2], z: List[Point2], l: int, r: int) -> Pair:
    # 两点的情况
    if r-l == 1:
        return Pair(x[l], x[r], dist(x[l], x[r]))
    # 三点的情况
    if r-l == 2:
        d1 = dist(x[l], x[l+1])
        d2 = dist(x[l+1], x[r])
        d3 = dist(x[r], x[l])

        if d1 <= d2 and d1 <= d3:
            return Pair(x[l], x[l+1], d1)
        elif d2 <= d3:
            return Pair(x[l+1], x[r], d2)
        else:
            return Pair(x[l], x[r], d3)
    # 多于三点, 分治法
    # l, r 中点
    m = (l+r) >> 1
    f = l
    g = m+1
    for i in range(l, r+1):
        if y[i].p > m:
            z[g] = y[i]
            g += 1
        else:
            z[f] = y[i]
            f += 1

    # 左右两部分递归求解
    best: Pair = closest_pair(x, z, y, l, m)  # 左半部分
    right: Pair = closest_pair(x, z, y, m+1, r)  # 右半部分

    if right.dist < best.dist:
        best = right

    # 重构数组 y
    # MergeSort.merge(z, y ,l, m, r) ??

    # d 矩形条内的点 置于 z 中
    k = l
    for i in range(l, r+1):
        if abs(x[m].x - y[i].x) < best.dist:
            z[k] = y[i]
            k += 1

    # 搜索 z[l: k]
    for i in range(l, k):
        for j in range(i+1, k):
            if z[j].y - z[i].y < best.dist:
                dp = dist(z[i], z[j])
                if dp < best.dist:
                    best = Pair(x[z[i].p], x[z[j].p], dp)

    return best


if __name__ == "__main__":
    x = [Point1(10, 2, 4), Point1(2, 3, 5), Point1(5, 9, 6), Point1(2, 2, 7)]
    pair = cpair2(x)
    print(pair)
