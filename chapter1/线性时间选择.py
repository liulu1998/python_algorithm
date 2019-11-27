# -*- encoding: utf-8 -*-
"""
@File    : 线性时间选择.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
import array
from typing import List


def select(a: list, left: int, right: int, k: int) -> int or float:
    """
    线性时间选择, 在 O(n)时间内找到数组第k小的数

    :param a: array like, 无序数组 
    :param left: int, 查找范围起始索引
    :param right: int, 查找范围结束索引
    :param k: int, 第k小
    :return int or float , 第k小的元素
    """
    if left == right:
        return a[left]
    # 划分位置
    p = partition(a, left, right)
    # 划分元素左部的元素数 (比划分元素小的元素数)
    num = p - left + 1

    if k == num:
        return a[p]
    elif k < num:          # 要找的元素在左部
        return select(a, left, p, k)
    else:               # 要找的元素在右部
        return select(a, p+1, right, k-num)


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
    a = array.array('i', [1, 90, 45, 3, 2, 56, 8, 70, 48])

    # a = [float(i) for i in input("输入浮点型或整型数组, 元素以空格间隔, 回车结束\n").split()]
    # position = int(input("输入查找第几小的元素, 整型\n"))
    # print(f"array:\n{a}")

    # 找到第 6 小的元素
    position = 5

    value = select(a, 0, len(a)-1, position)
    print(f"\nsorted a:\n{sorted(a)}\n")

    print(f"k:{position}\nvalue:{value}")
