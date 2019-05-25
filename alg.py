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
ip_str = "1921840187"
ip_lst = list(ip_str) #str -> list
fields = {} #key:0-3, value:str
def search_Ip(ips,prev,dep):
    if dep == 4:
        tmp = [v for k,v in prev.items()]
        if "".join(tmp) != ips:
            return
        else:
            print(".".join(tmp))
    cur = [v for k,v in prev.items() if k < dep]
    cur_str = "".join(cur)
    for i in range(len(cur_str)+1,len(ips)+1,1):
        if verifyStr(ips[len(cur_str):i]):
            prev[dep] = ips[len(cur_str):i]
            search_Ip(ips,prev,dep+1)


def verifyStr(i_str):
    num = int(i_str)
    if num >= 0 and num <= 255:
        return True
    else:
        return False

search_Ip(ip_str, fields, 0)


##回溯算法：0-1背包问题，每个物品重量不同且价值也不同，在不超过背包重量的情况下，如何使得装进背包的物品总价值最大
b_weight = 20 #背包重量
item_w = {0:3,1:5,2:10,3:8,4:1,5:6} # key:物品 value:weight
item_m = {0:6,1:20,2:5,3:7,4:3,5:4} # key:物品 value:money
max_value = -1
choose = {} #是否选择物品，物品:0/1，0是未选择，1是选择
bag_value_choose = {}
def bagpack(i, cw, cm, item_weight, item_money, bag_w, n):
    if cw == bag_w or i == n:
        global max_value
        global bag_value_choose
        if cm > max_value:
            max_value = cm
            bag_value_choose = {k:v for k,v in choose.items()}
        return
    choose[i] = 0
    bagpack(i+1,cw,cm,item_weight,item_money,bag_w,n)
    if (cw+item_weight[i]) <= bag_w:
        choose[i] = 1
        bagpack(i+1,cw+item_weight[i],cm+item_money[i],item_weight,item_money,bag_w,n)

bagpack(0,0,0,item_w,item_m,b_weight,6)
print(max_value,end="->")
print(bag_value_choose)

##动态规划：0-1背包问题，每个物品重量不同且价值也不同，在不超过背包重量的情况下，如何使得装进背包的物品总价值最大
##动态规划的思路：把问题分为n个阶段，依次考察每个阶段的状态集合（去除重复的），由当前的状态集合推导下一个阶段的状态集合，动态地往前推进
weight_values = {}  #key/value -> 重量/当前重量的最大价值
def bag_dynamic_program(bag_w, n):
    for i in range(bag_w+1):
        weight_values[i] = -1
    #初始化第一个物品
    weight_values[0] = 0
    weight_values[3] = 6
    for i in range(1,n,1):  #依次考察其他的物品
        j = bag_w - item_w[i]
        while j >= 0:
            if weight_values[j] >= 0:
                v = weight_values[j] + item_m[i]
                if v > weight_values[j+item_w[i]]:
                    weight_values[j+item_w[i]] = v
            j = j - 1

    values = [v for k,v in weight_values.items()]
    values.sort()
    return values[len(values)-1]

print(bag_dynamic_program(b_weight,6),end="->")
print(weight_values)
