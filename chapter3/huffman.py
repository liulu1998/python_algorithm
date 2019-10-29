from queue import PriorityQueue
from typing import List
import matplotlib.pyplot as plt


class Node(object):
    def __init__(self, weight: float, char: str, left, right):
        """构造器
        :param weight: float, 节点权重（频率）
        :param char: str, 节点字符
        :param left: Node, 左孩子
        :param right: Node, 右孩子
        """
        self.weight = weight
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        """小于方法
        """
        return self.weight < other.weight

    def __le__(self, other):
        """小于等于方法
        """
        return self.weight <= other.weight

    def __str__(self):
        return f"{self.weight} {self.char}" 


def huffman(chars: List[str], freqs: List[float]) -> Node:
    """构造哈夫曼树
    :param chars: List[str], 字符数组
    :param freqs: List[float], 字符对应的频率数组
    :return Node, 构造好的哈夫曼树
    """
    pq = PriorityQueue()
    for (f, c) in zip(freqs, chars):
        pq.put(Node(weight=f, char=c, left=None, right=None))
    
    while len(pq.queue) > 1:
        left: Node = pq.get()
        right: Node = pq.get()
        father = Node(left.weight+right.weight, None, left, right)
        pq.put(father)

    return pq.queue[0]

if __name__ == "__main__":
    chars = ["a", "b", "c", "d"]
    freqs = [0.5, 0.2, 0.2, 0.1]

    tree = huffman(chars, freqs)

