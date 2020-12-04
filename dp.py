# -*- coding: utf-8 -*-

b_weight = 20 #背包重量
item_w = {0:3,1:5,2:10,3:8,4:1,5:6} # key:物品 value:weight
item_m = {0:6,1:20,2:5,3:7,4:3,5:4} # key:物品 value:money

max_v = -1
max_items = None

'''
暴力解法
每个item共有2种状态：选、不选；
考察这些item所有可能状态的组合，计算每种组合的weight和value，并从中选取符合条件的最优解。
'''
for i in range(64):
    selector = {}
    for j in range(6):
        if ((i>>j) & 0x01) == 1:
            selector[j] = 1
        else:
            selector[j] = 0
    print('{}:{}'.format(i,selector))
    cw = 0
    cv = 0
    for k,v in selector.items():
        if v == 1:
            cw += item_w[k]
            cv += item_m[k]
    if cw <= b_weight and cv > max_v:
        max_v = cv
        max_items = {k:v for k,v in selector.items()}


print('max_v:{}'.format(max_v))
print('max_items:{}'.format(max_items))

'''
上述的暴力解法，效率较低。
原因在于：
  1、所有item的可能状态的组合比较多，计算量大；
  2、有些计算是重复的，比如相同value的情况，对于不同的weight组合计算了多次；
  3、有些计算是多余的，比如weight超过了约束条件，value其实没必要计算；
其实在计算中，存在着相同的状态，这个状态就是：{重量，当前重量的最大价值}
'''

'''
给定矩阵A，A[i][j]描述在这个位置的宝石数，我们需要在每一行取一个宝石使得最后的宝石数最多，
但是注意，从第(i,s)位置到第(i+1,t)位置需要消耗宝石，消耗量为|t-s|。

暴力解法：逐行搜索元素
'''
import math
A = [[1,2,3],[6,5,4],[9,8,7]]
path = None
max_G = -1
def searchGem(arr, row, colNum, rowNum, prev, cv, lujing):
    global max_G
    global path
    if rowNum == row:
        if cv > max_G:
            max_G = cv
            path = [(k,v) for k,v in lujing.items()]
        return
    for i in range(colNum):
        tmp = cv
        tmp += arr[row][i]
        if prev != None:
            tmp = tmp - int(math.fabs(prev[1]-i))
        lujing[row] = i
        searchGem(arr, row+1, colNum, rowNum, [row,i], tmp, lujing)

searchGem(A,0,3,3,None,0,{})
print('max gems: {}, path:{}'.format(max_G,path))

'''
记录状态：[位置，最大gem数]
'''
def dp_gem(arr):
    pos_gem = [arr[0],[0,0,0],[0,0,0]]
    for r in range(1,3):
        for c in range(3):
            prev_r = r - 1
            pos_gem[r][c] += arr[r][c]
            max_gems = -1
            for k in range(3):
                tmp = pos_gem[r][c] + pos_gem[prev_r][k] - int(math.fabs(k-c))
                if tmp > max_gems:
                    max_gems = tmp
            pos_gem[r][c] = max_gems
    print('{}'.format(pos_gem))
    result = []
    for _,v in enumerate(pos_gem):
        result.extend(v)
    result.sort()
    print('max gems: {}'.format(result[-1]))

dp_gem(A)