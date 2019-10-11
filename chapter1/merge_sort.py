import numpy as np
from typing import List


def merge_sort(a: List[int], left: int, right: int) -> None:
    """
    归并排序

    :param a
        array like, 待排序数组
    :param left
        int, 起始索引
    :param right
        int, 结束索引
    :return None
    """
    if left == right:
        return
    middle: int = (left + right) >> 1
    merge_sort(a, left, middle)
    merge_sort(a, middle+1, right)
    merge(a, left, right)


def merge(a: List[int], left: int, right: int) -> None:
    """
    左右部分分别有序的数组, 归并为一个有序数组, 覆盖原数组(in-place)

    :param a
        array like, 待归并数组
    :param left
        int, 归并范围的起始索引
    :param right
        int, 归并范围的结束索引
    :return None
    """
    # 暂存归并结果的数组
    m = np.empty((right-left+1, ), dtype=np.int32)
    # 待归并的数组 a 的中间索引
    mid: int = (left + right) >> 1
    # 左半部分、右半部分、归并结果的游标
    index_l: int = left
    index_r: int = mid + 1
    index_m: int = 0

    while(index_l < mid+1 and index_r < right+1):
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
    a[left: right+1] = m


if __name__ == "__main__":
    # 11 个整型元素, 值介于0和80
    a = np.random.randint(80, size=11)
    print(f"original array:\n{a}")

    # 原地归并排序
    merge_sort(a, 0, len(a)-1)
    print(f"after merge-sort:\n{a}")
