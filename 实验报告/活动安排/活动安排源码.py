# -*- encoding: utf-8 -*-
"""
@File    : 活动安排.py
@Version : 1.0
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""
from typing import List
from collections import namedtuple


def greedy_selector(s: List[int], f: List[int]) -> (int, List[bool]):
    """
    活动安排

    :param s: 起始时间列表
    :param f: 结束时间列表, 元素非递减
    :return int: 最大相容的活动数
    :return List[bool]: 每个活动是否被安排
    """
    if len(s) != len(f):
        raise ValueError("length not equal")

    # 每个活动是否被安排
    result = [ False for i in range(len(s))]
    result[0] = True
    # 安排的活动数
    count = 1

    j = 0
    for i in range(1, len(s)):
        if s[i] >= f[j]:
            result[i] = True
            j = i
            count += 1
        # else:
        #     a[i] = False
    return count, result

class Act:
    def __init__(self, s: int, f: int):
        if f <= s:
            raise ValueError("开始时间应小于结束时间")
        self.s = s
        self.f = f
    
    def __lt__(self, other):
        return self.f < other.f


if __name__ == "__main__":
    # s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    # f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    s = [int(i) for i in input("依次输入活动开始时间(整型), 空格分隔, 回车结束\n").split()]
    f = [int(i) for i in input("依次输入活动开始时间(整型), 空格分隔, 回车结束\n").split()]
    
    try:
        acts = [Act(ss, ff) for ss, ff in zip(s, f)]
        acts.sort()
    except Exception as e:
        print(e)
        exit()

    s = [act.s for act in acts]
    f = [act.f for act in acts]


    count, result = greedy_selector(s, f)
    
    print(f"count: {count}\n{result}")
    # out:
    # count: 4
    # [True, False, False, True, False, False, False, True, False, False, True]
