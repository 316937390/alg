# -*- coding: utf-8 -*-
from __future__ import print_function ##使用python3中给end参数赋空(值)的方式实现输出不换行

##循环有序数组中查找
lst = [4,5,6,1,2,3]
def find(a, low, high, value):
    while low <= high:
        mid  = low + (high-low)/2
        if a[mid] == value:
            return mid
        ##前半部分是有序的，后半部分是循环有序
        elif a[low] <= a[mid]:
            if a[mid] > value and a[low] <= value:
                high = mid - 1
            else:
                return find(a,mid+1, high,value)
        ##后半部分是有序的，前半部分是循环有序的
        elif a[low] > a[mid]:
            if a[mid] < value and a[high] >= value:
                low = mid + 1
            else:
                return find(a,low,mid-1,value)
    return -1

print(find(lst,0,len(lst)-1,4))
print(find(lst,0,len(lst)-1,5))
print(find(lst,0,len(lst)-1,6))
print(find(lst,0,len(lst)-1,1))
print(find(lst,0,len(lst)-1,2))
print(find(lst,0,len(lst)-1,3))
print(find(lst,0,len(lst)-1,7))

import Queue
"""
q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
"""
##图：邻接表存储
graph = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5,6],5:[2,4,7],6:[4,7],7:[5,6]}
##广度优先搜索：用户的3度好友关系
def bfs(s,deg):
    v = 8 #顶点个数
    visited = {}
    prev = {}
    que = Queue.Queue()
    for i in range(v):
        visited[i] = False
        prev[i] = -1
    que.put(s)
    visited[s] = True
    dist = {} ##记录每个顶点与s的距离
    dist[s] = 0
    friends = []
    while not que.empty():
        ele = que.get()
        for i in graph.get(ele):
            if not visited.get(i):
                dist[i] = dist[ele]+1
                if dist[i] > deg:
                    break
                prev[i] = ele
                visited[i] = True
                que.put(i)
                friends.append(i)
    return friends,prev

print(bfs(1,2))

##深度优先搜索：用户的3度好友关系
def dfs(s,deg):
    v = 8 #顶点个数
    visited = {}
    prev = {}
    friends = []
    for i in range(v):
        visited[i] = False
        prev[i] = -1
    recurDfs(s,deg,visited,prev,friends,0)
    return friends,prev

def recurDfs(s,deg,visited,prev,friends,dep):
    if dep > deg:
        return
    visited[s] = True
    if dep > 0:
        friends.append(s)
    for i in graph.get(s):
        if not visited.get(i):
            prev[i] = s
            recurDfs(i,deg,visited,prev,friends,dep+1)

print(dfs(1,2))




##分治算法：二维平面上有 n 个点，如何快速计算出两个距离最近的点对？
dots = [(1,2),(2,5),(4,3),(6,2)]
"""
(1,2),(2,5) = 10
(1,2),(4,3) = 10
(1,2),(6,2) = 25
(2,5),(4,3) = 8
(2,5),(6,2) = 25
(4,3),(6,2) = 5
"""

##分治算法：有两个 n*n 的矩阵 A，B，如何快速求解两个矩阵的乘积 C = A*B？
##需要定义矩阵加法操作
A = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
B = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
def matrix_multiply(A, B, start_row_A, end_row_A, start_col_A, end_col_A, start_row_B, end_row_B, start_col_B, end_col_B):
    row_A_split = start_row_A + (end_row_A-start_row_A)/2
    row_B_split = start_row_B + (end_row_B-start_row_B)/2
    col_A_split = start_col_A + (end_col_A-start_col_A)/2
    col_B_split = start_col_B + (end_col_B-start_col_B)/2
    matrix_multiply(A,B,start_row_A,row_A_split,start_col_A,col_A_split,start_row_B,row_B_split,start_col_B,col_B_split) + 0 #TODO:矩阵加法

##回溯算法：八皇后问题
result = {} ##queen放置的位置，key:行，value:列
def cal8Queen(row):
    if row == 8:
        printQueens(result)
        return
    for col in range(8): #每行有8列，依次尝试放到这8个位置
        if isOk(row,col):
            result[row] = col #queen放置在row行的col列
            cal8Queen(row+1)

def isOk(r,c):
    #逐层往上考察每一行
    r = r - 1
    leftup = c - 1
    rightup = c + 1
    while r >= 0:
        if result[r] == c:
            return False
        if leftup >= 0 and result[r] == leftup:
            return False
        if rightup < 8 and  result[r] == rightup:
            return False
        r = r - 1
        leftup = leftup - 1
        rightup = rightup + 1
    return True

def printQueens(res):
    for i in range(8):
        for j in range(8):
            if res[i] == j:
                print("Q ",end="")
            else:
                print("* ",end="")
        print("")
    print("")

cal8Queen(0)


##回溯算法：ip字符串找出所有合法的ip地址
