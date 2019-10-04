import numpy as np
from typing import List


def binary_search(a: List[int], x: int, n: int) -> int:
    """
    二分搜索

    :param a
        array like, 有序数组
    :param x
        int, 待搜索的值
    :param n
        int, 搜索范围 [0..n-1]
    """

    left = 0
    right = n-1
    while(left <= right):
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
