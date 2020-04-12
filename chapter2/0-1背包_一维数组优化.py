# -*- encoding: utf-8 -*-
"""
@File    : 0-1背包_一维数组优化.py
@Author  : Liu Lu
@Email   : liulu_heu@qq.com
@Software: PyCharm
"""

if __name__ == '__main__':
    n: int      # 物品数
    m :int     # 背包最大容量

    f = [0] * m     # dp 数组, 一维数组优化

    # 在线求解
    for i in range(1, n+1):
        v = int(input("输入物品体积"))
        w = int(input("输入物品价值"))
        for j in range(m, v - 1, -1):   # 自大到小循环
            f[j] = max(f[j], f[j - v] + w)

    # 最大价值
    print(f[m])
