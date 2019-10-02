import numpy as np


def min_weight_triangulation(weight: np.ndarray, w):
    # 多边形顶点数
    n = weight.shape[0]
    # 存储子问题最优值
    t = np.empty((n, n), dtype=np.int32)
    s = np.empty((n, n), dtype=np.int8)

    for i in range(0, n):
        t[i][i] = 0
    
    for col in range(1, n):
        for row in range(0, n-col):
            cur_col = row + col
            
            t[row][cur_col] = t[row+1][cur_col] + w(weight, row, row+1, cur_col) 
            s[row][cur_col] = row

            # 计算划分最优位置 k
            for k in range(row+1, cur_col):
                tmp_t = t[row][k] + t[k+1][cur_col] + w(weight, row, k+1, cur_col) 
                # 如果出现更优的划分位置 k
                if tmp_t < t[row][cur_col]:
                    s[row][cur_col] = k
                    t[row][cur_col] = tmp_t
    return t, s

def traceback(s: np.ndarray, i: int, j: int) -> None:
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f"划分的三角形 V{i} V{j} V{s[i][j]}")


def w(weight: np.ndarray, a: int, b: int, c:int) -> int:
    return weight[a][b] + weight[b][c] + weight[a][c]


if __name__ == "__main__":
    weight = [
        [0,2,2,3,1,4],
		[2,0,1,5,2,3],
		[2,1,0,2,1,4],
		[3,5,2,0,6,2],
		[1,2,1,6,0,1],
	    [4,3,4,2,1,0]
    ]

    weight = np.array(weight, dtype=np.int32)
    t, s = min_weight_triangulation(weight, w)

    print(t, s, sep="\n\n")
    traceback(s, 0, len(weight)-1)
