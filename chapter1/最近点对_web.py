from math import sqrt
 
def nearest_dot(s):
    len = s.__len__()
    left = s[0:len/2]
    right = s[len/2:]
    mid_x = (left[-1][0]+right[0][0])/2.0
 
    if left.__len__() > 2:   lmin = nearest_dot(left)    #左侧部分最近点对
    else:   lmin = left
    if right.__len__() > 2:   rmin = nearest_dot(right)   #右侧部分最近点对
    else:   rmin = right
 
    if lmin.__len__() >1: dis_l = get_distance(lmin)
    else: dis_l = float("inf")
    if rmin.__len__() >1: dis_2 = get_distance(rmin)
    else: dis_2 = float("inf")
 
    d = min(dis_l, dis_2)   #最近点对距离
 
    mid_min=[]
    for i in left:
        if mid_x-i[0]<=d :   #如果左侧部分与中间线的距离<=d
            for j in right:
                if abs(i[0]-j[0])<=d and abs(i[1]-j[1])<=d:     #如果右侧部分点在i点的(d,2d)之间
                    if get_distance((i,j))<=d: mid_min.append([i,j])   #ij两点的间距若小于d则加入队列
    if mid_min:
        dic=[]
        for i in mid_min:
            dic.append({get_distance(i):i})
        dic.sort(key=lambda x: x.keys())
        return (dic[0].values())[0]
    elif dis_l>dis_2:
        return rmin
    else:
        return lmin
 
# 求点对的距离
def get_distance(min):
    return sqrt((min[0][0]-min[1][0])**2 + (min[0][1]-min[1][1])**2)
 
def divide_conquer(s):
    s.sort(cmp = lambda x,y : cmp(x[0], y[0]))
    nearest_dots = nearest_dot(s)
    print(nearest_dots)

if __name__ == "__main__":
     x = [
        (0, 1), (3, 2),
        (4, 3), (5, 1),
        (2, 1), (1, 2),
        (6, 2), (7, 2), 
        (8, 3), (4, 5), 
        (9, 0), (6, 4)]
     divide_conquer(x)
