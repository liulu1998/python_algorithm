from typing import List


class Knapsack:
    def __init__(self, c: float, w: List[float], p: List[float]):
        """
        0-1背包类构造器
        
        :param c: float, 背包容量
        :param w: List[float], 物品重量
        :param p: List[float], 物品价值
        """
        if len(w) != len(p):
            raise ValueError("价值数组应与重量数组等长")
        self.c = c
        self.w = w
        self.p = p
        # 物品总数
        self.n = len(w)
        # 背包当前重量
        self.cw = 0.0
        # 背包当前价值
        self.cp = 0.0
        # 背包当前最优价值
        self.bestp = 0.0
    
    def Knapsack(self) -> List[bool]:
        """
        回溯法求解 0-1背包问题

        :return List[bool], 解向量, 对应每个物品是否装入
        """
        
