from queue import PriorityQueue
from typing import List


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

    def __lt__(self, other) -> bool:
        """小于方法
        """
        return self.weight < other.weight

    def __le__(self, other) -> bool:
        """小于等于方法
        """
        return self.weight <= other.weight

    def __str__(self) -> str:
        """转为字符串方法
        """
        return f"[{self.weight:.3f} {self.char}]" 


def huffman(chars: List[str], freqs: List[float]) -> Node:
    """构造哈夫曼树
    :param chars: List[str], 字符数组
    :param freqs: List[float], 字符对应的频率数组
    :return Node, 构造好的哈夫曼树
    """
    if len(chars) != len(freqs):
        raise ValueError("权重数组与字符数组不等长!")
    # 优先队列, 由小顶堆实现
    pq = PriorityQueue()
    # 初始化叶子节点, 加入优先队列
    for f, c in zip(freqs, chars):
        pq.put(Node(weight=f, char=c, left=None, right=None))
    
    while len(pq.queue) > 1:
        left = pq.get()
        right = pq.get()
        # 构造父节点, 权值为子节点权值之和
        parent = Node(left.weight+right.weight, None, left, right)
        pq.put(parent)

    return pq.queue[0]


if __name__ == "__main__":
    chars = ["a", "b", "c", "d"]
    freqs = [0.5, 0.2, 0.2, 0.1]

    tree = huffman(chars, freqs)
