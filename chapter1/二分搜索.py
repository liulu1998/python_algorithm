# -*- encoding: utf-8 -*-
"""
@File    : binary_search.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
from typing import List
import numpy as np


def binary_search(a: List[float], x: int, n: int) -> int:
    """
    二分搜索
    :param a, array like, 有序数组
    :param x, int, 待搜索的值
    :param n, int, 搜索范围 [0..n-1]
    :return int, 若搜索到返回元素索引; 否则返回 -1
    """

    left = 0
    right = n-1
    while left <= right:
        middle = (left + right) >> 1
        if a[middle] == x:
            return middle
        elif x > a[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    # a: from 1 to 10
    a = np.arange(1, 11, dtype=np.int8)

    for x in range(-3, 13):
        print(f"search: {x}  index: {binary_search(a, x, len(a))}")

    # out:
    # search: -2  index: -1
    # search: -1  index: -1
    # search: 0  index: -1
    # search: 1  index: 0
    # search: 2  index: 1
    # search: 3  index: 2
    # search: 4  index: 3
    # search: 5  index: 4
    # search: 7  index: 6
    # search: 9  index: 8
    # search: 10  index: 9
    # search: 11  index: -1
