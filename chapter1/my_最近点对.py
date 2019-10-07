from math import sqrt
import numpy as np
from typing import List


def dist(x, y) -> float:
    """计算两点的欧式距离
    """
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2) 


def cpair2(s):
    """
    二维最接近点对
    """
    if len(s) < 2:
        return None
    # x 坐标中位数
    mid_x = (min(s[:, 0]) + max(s[:, 0])) / 2
    # 根据 x坐标中位数, 将 S 划分为两半
    s1 = s[s[:, 0] <= mid_x, :]
    s2 = s[s[:, 0]  > mid_x, :]


if __name__ == "__main__":
    S = [
        [1, 3],
        [5, 8], 
        [2, 100],
        [4, 10]
    ]

    S = np.array(S, dtype=np.float32)
