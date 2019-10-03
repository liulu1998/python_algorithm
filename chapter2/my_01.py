import numpy as np
from typing import List


def knapstack(values: List[int], weights: List[int], c: int) -> np.ndarray:
    """
    计算子问题最优值m[i][j]

    :param v
        array like, 物品价值数组
    :param w
        array like, 物品重量数组
    :param c
        float, 背包容量
    :return m
        2D array, 子问题最优值矩阵
    """
    # 初始化m矩阵 及其边界
    m = np.empty((len(values)+1, c+1), dtype=np.int32)
    m[0, :] = 0
    m[:, 0] = 0

    for i in range(1, len(values)):
        for j in range(1, c+1):
            if j < weights[i-1]:
                m[i][j] = 0
            

 
