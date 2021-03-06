from typing import List
import numpy as np


def merge_sort(a: List[int]) -> None:
    """
    归并排序, 非递归，in-place

    :param a: array like, 待排序数组
    :return None
    """
    # 相邻子数组长度
    i = 1
    while(i < len(a)):
        low = 0
        # 相邻子数组, 两两归并
        while(low < len(a)):
            merge(a, left=low, mid=low+i-1, right=min(low+2*i-1, len(a)-1))
            low += 2*i
        # 子数组长度加倍
        i = i << 1


def merge(a: List[int], left: int, mid: int, right: int) -> None:
    """
    左右部分分别有序的数组, 归并为一个有序数组, in-place

    :param a, array like, 待归并数组
    :param left, int, 归并范围的起始索引
    :param mid, int, 两个相邻子数组的分界
    :param right, int, 归并范围的结束索引
    :return None
    """
    # 暂存归并结果的数组
    m = np.empty((right-left+1, ), dtype=np.int32)
    # 待归并的数组 a 的中间索引
    
    # 左半部分、右半部分、归并结果的游标
    index_l: int = left
    index_r: int = mid + 1
    index_m: int = 0

    while(index_l < mid + 1 and index_r < right + 1):
        if a[index_l] <= a[index_r]:
            m[index_m] = a[index_l]
            index_l += 1
        else:
            m[index_m] = a[index_r]    
            index_r += 1
        # 归并结果的游标后移
        index_m += 1

    # 左半部分先归并结束, 右半部分接到数组最后
    # if index_l == mid + 1:
    #     m[index_m: len(m)] = a[index_r: right+1]
    # else:
    #     m[index_m: len(m)] = a[index_l: mid+1]

    m[index_m: len(m)] = a[index_r: right+1] if (index_l == mid + 1) else a[index_l: mid+1]
    # 覆盖a
    a[left: right+1] = m


if __name__ == "__main__":
    # 值介于0~80, 
    a = np.random.randint(80, size=11)
    print(f"original array:\n{a}")

    merge_sort(a)
    print(f"after merge-sort:\n{a}")
