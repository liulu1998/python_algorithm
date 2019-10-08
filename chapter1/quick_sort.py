import numpy as np
from typing import List


def quick_sort_pythonic(array: List[int]) -> List[int]:
    """
    python风格的快速排序, 但空间复杂度较高

    :param array: array like, 待排序数组
    :return List[int], 有序数组
    """

    if len(array) <= 1:
        return array

    x = array.pop()
    lower, greater = [], []
    for a in array:
        if a > x:
            greater.append(a)
        else:
            lower.append(a)
    return quick_sort_pythonic(lower) + [x] + quick_sort_pythonic(greater)


def quick_sort(a: List[int], p: int, r: int) -> None:
    """
    快速排序

    :param a: List[int], 待排序数组
    :param p: int, 排序范围 起始索引
    :param r: int, 排序范围 结束索引
    :return None, 覆盖原数组
    """
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


def partition(a: List[int], p: int, r: int) -> int:
    """
    快速排序 - 划分

    :param a: List[int], 待划分数组
    :param p: int, 划分范围 起始索引
    :param r: int, 划分范围 结束索引 
    """
    low = p
    high = r
    x = a[p]

    while low < high:
        while low < high and a[high] >= x:
            high -= 1

        if low < high:
            a[low] = a[high]
            low += 1
        
        while low < high and a[low] < x:
            low += 1
        
        if low < high:
            a[high] = a[low]
            high -= 1
            
    a[high] = x
    return high


if __name__ == "__main__":
    a = np.random.randint(50, size=11)
    # b = list(a)

    # 原始数组
    print(a)

    quick_sort(a, 0, len(a)-1)
    print(a)

    # 返回 b 的副本
    # b = quick_sort_pythonic(b)
    # print(b)
