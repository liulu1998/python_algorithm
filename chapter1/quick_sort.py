import numpy as np
from typing import List


def quick_sort(a: List[int], p: int, r: int) -> None:
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


def partition(a: List[int], p: int, r: int) -> int:
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
    a = np.random.randint(30, size=10)
    print(a)
    quick_sort(a, 0, len(a)-1)
    print(a)
