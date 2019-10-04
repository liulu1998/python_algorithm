import numpy as np
from typing import List


def merge_sort(a: List[int]) -> None:
    b = np.empty((len(a), ), dtype=np.int32)

    s = 1
    while(s < len(a)):
        merge_pass(a, b, s)
        s<<1
        merge_pass(b, a, s)
        s<<1


def merge_pass(x: List[int], y: List[int], s: int) -> None:
    """
    合并大小为 s 的相邻子数组
    """
    i = 0
    # 合并大小为s 的相邻 2段子数组
    while i <= (len(x) - 2*s):
        merge(x, y, i, i+s-1, i+2*s-1)
        # i = i + 2*s
        i += 2*s
    # 剩下的元素数小于 2s
    if i+s < len(x):
        merge(x, y, i, i+s-1, len(x)-1)
    else:
        # 复制到 y
        y[i: len(x)] = x[i: len(x)]



def merge(a: List[int], b: List[int], left: int, mid: int, right: int) -> None:
    """
    左右部分分别有序的数组a, 归并为一个有序数组b

    :param a
        array like, 待归并数组
    :param b
        array like
    :param left
        int, 归并范围的起始索引
    :param right
        int, 归并范围的结束索引
    :return None
    """
    # 左半部分、右半部分、归并结果的游标
    i = 0
    j = mid+1
    k = left

    while(i <= mid and j <= right):
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1

    if i > mid:
        for q in range(j, right+1):
            b[k] = a[q]
            k += 1
    else:
        for q in range(i, mid+1):
            b[k] = a[q]
            k += 1


if __name__ == "__main__":
    a = np.random.randint(20, size=11)
    print(a)
    merge_sort(a)

    print(a)