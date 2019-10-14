import numpy as np
from typing import List


def select(a: list, left: int, right: int, k: int) -> int or float:
    """
    线性时间选择, 在 O(n)时间内找到数组第k小的数

    :param a: array like, 无序数组 
    :param left: int, 查找范围起始索引
    :param right: int, 查找范围结束索引
    :parma k: int, 第k小
    :return int or float , 第k小的元素
    """
    if left == right:
        return a[left]
    # 划分位置
    i = partition(a, left, right)
    # 左部的元素数
    j = i - left + 1
    # 要找的元素在左部
    if k <= j:
        return select(a, left, i, k)
    else:
        return select(a, i+1, right, k-j)


def partition(a: list, p: int, r: int) -> int:
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
    # 元素介于 0~80, 11个元素的整型数组
    a = np.random.randint(80, size=11)

    # 找到第 6 小的元素
    position = 6

    print(f"array:\n{a}\n\nsorted a:\n{sorted(a)}")

    print(select(a, 0, len(a)-1, position))
