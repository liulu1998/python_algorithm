# -*- encoding: utf-8 -*-
"""
@File    : 凸多边形最优三角剖分.py
@Version : 1.0
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
import numpy as np
from typing import Callable


def min_weight_triangulation(weight: np.ndarray, w: Callable[[int, int, int], int]) -> (np.ndarray, np.ndarray):
    """
    计算最优值t, 最优值对应的划分位置s

    :param weight
        2D array, 多边形的权值(边长)
    :param w
        function, 三角形权值计算公式
    :return s
        2D array, s[i][j] 为 子多边形{ V(i-1), V(i)... V(j) } 划分的最优值
    :return t
        2D array, t[i][j] 为 s[i][j]对应的最优划分位置 
    """
    # 多边形顶点数
    n = weight.shape[0]
    # 存储子问题最优值
    t = np.empty((n, n), dtype=np.int32)
    s = np.empty((n, n), dtype=np.int8)

    for i in range(1, n):
        t[i][i] = 0
    
    for col in range(2, n):
        for row in range(1, n-col+1):
            # 自左上向右下计算
            cur_col = row + col - 1

            t[row][cur_col] = t[row+1][cur_col] + w(weight, row-1, row, cur_col)
            s[row][cur_col] = row

            # 计算划分最优位置 k
            for k in range(row+1, cur_col):
                tmp_t = t[row][k] + t[k+1][cur_col] + w(weight, row-1, k, cur_col) 
                # 如果出现更优的划分位置 k
                if tmp_t < t[row][cur_col]:
                    s[row][cur_col] = k
                    t[row][cur_col] = tmp_t
    return t, s

def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f"划分的三角形 V{i-1} V{j} V{s[i][j]}")


def w(weight: np.ndarray, a: int, b: int, c:int) -> int:
    return weight[a][b] + weight[b][c] + weight[a][c]


if __name__ == "__main__":    
    # 顶点数
    n = np.random.randint(low=4, high=8)
    weight = np.random.randint(low=1, high=30, size=(n, n))
    
    for i in range(n):
        weight[i][i] = 0
    # 构造为对称阵
    for i in range(n):
        for j in range(i+1, n):
            weight[j][i] = weight[i][j] 
    
    print("邻接矩阵:")
    for wxx in weight:
        print(list(wxx))
    
    weight = np.array(weight, dtype=np.int32)

    t, s = min_weight_triangulation(weight, w)

    traceback(s, 1, len(weight)-1)
    # weight = [
    #     [0,2,2,3,1,4],
	# 	[2,0,1,5,2,3],
	# 	[2,1,0,2,1,4],
	# 	[3,5,2,0,6,2],
	# 	[1,2,1,6,0,1],
	#     [4,3,4,2,1,0]
    # ]
    # out:
    # 划分的三角形 V2 V4 V3
    # 划分的三角形 V1 V4 V2
    # 划分的三角形 V0 V4 V1
    # 划分的三角形 V0 V5 V4
