# -*- coding: utf-8 -*-
from __future__ import print_function ##使用python3中给end参数赋空(值)的方式实现输出不换行

##循环有序数组中查找
lst = [4,5,6,1,2,3]
def find(a, low, high, value):
    while low <= high:
        mid  = low + ((high-low)>>1)
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

from queue import Queue
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
    que = Queue()
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


##动态规划：满足“一个模型三个特征”
##“一个模型”：多阶段决策最优解模型
##“三个特征”：最优子结构，无后效性，重复子问题
##动态规划的一般思考过程：状态转移表法，状态转移方程法（递归加备忘录 或 迭代递推）
##动态规划：杨辉三角，求从最高层到最底层的最短路径长度
yh = [[5,8,4,1,5],[7,3,6,4],[2,9,9],[4,7],[2]]
#初始化最短路径长度矩阵，即“备忘录”
Mins = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1],[-1,-1],[-1]]
def minDist(i,j):
    if i == 0 and j == 0:
        return yh[0][0]
    if Mins[i][j] > 0:
        return Mins[i][j]
    # 只能向下或向右走，即i+1或j+1
    up = False
    up_min = -1
    left = False
    left_min = -1
    if i - 1 >= 0 :
        up = True
        up_min = minDist(i-1,j)
    if j - 1 >= 0:
        left = True
        left_min = minDist(i,j-1)
    if up and left:
        Mins[i][j] = yh[i][j] + min(up_min,left_min)
        return yh[i][j] + min(up_min,left_min)
    elif up == False and left == True:
        Mins[i][j] = yh[i][j] + left_min
        return yh[i][j] + left_min
    elif up == True and left == False:
        Mins[i][j] = yh[i][j] + up_min
        return yh[i][j] + up_min

print(minDist(4,0))
print(minDist(3,1))
print(minDist(2,2))
print(minDist(1,3))
print(minDist(0,4))


##硬币找零问题：回溯法
##三种面值的硬币：1，3，5，需要支付9元，求最少需要多少个硬币？
coin_values = [1,3,5]
value_num = {}
def coin_huisu(cv,num,total_value):
    if cv == total_value:
        if value_num.get(cv) == None:
            value_num[cv] = num
        else:
            if num < value_num.get(cv):
                value_num[cv] = num
        return
    for i in coin_values:
        if cv + i <= total_value:
            coin_huisu(cv+i,num+1,total_value)

coin_huisu(0,0,9)
print("回溯法：最少需要%d个硬币" % value_num.get(9))
##硬币找零问题：动态规划
##状态转移方程：f(9)=1+min(f(8),f(6),f(4))
coins_value_steps = {1:1,3:1,5:1}
def coin_dy(total_value):
    if coins_value_steps.get(total_value) != None:
        return coins_value_steps[total_value]
    if total_value - 1 > 0 and total_value - 3 > 0 and total_value - 5 > 0:
        return 1 + min(coin_dy(total_value-1),coin_dy(total_value-3),coin_dy(total_value-5))
    elif total_value - 1 > 0 and total_value - 3 > 0:
        return 1 + min(coin_dy(total_value - 1), coin_dy(total_value - 3))
    elif total_value - 1 > 0:
        return 1 + coin_dy(total_value - 1)
print("动态规划：最少需要%d个硬币" % coin_dy(9))


##编辑距离（edit distance）：量化两个字符串之间的相似程度，将一个字符串转化成另一个字符串需要的最少编辑操作次数
##莱文斯坦距离（差异程度）
##最长公共子串长度（相似程度）
##最长公共子串长度的回溯解法
a = "mitcmu"
b = "mtacnu"
m = len(a)
n = len(b)
maxV = -1
def lcs_huisu(i,j,mlen):
    if i == m or j == n:
        global maxV
        if mlen > maxV:
            maxV = mlen
        return
    if a[i] == b[j]:
        lcs_huisu(i+1,j+1,mlen+1)
    else:
        lcs_huisu(i+1,j,mlen)
        lcs_huisu(i,j+1,mlen)

lcs_huisu(0,0,0)
print("最长公共子串长度，回溯法：%d" % maxV)
#最长公共子串长度的动态规划解法
states_lcs = {0:{0:1}}
def lcs_dp(i,j):
    if i == 0 and j == 0:
        return states_lcs[0][0]
    if i < 0:
        return -1
    if j < 0:
        return -1
    if states_lcs.get(i) != None and states_lcs.get(i).get(j) != None:
        return states_lcs[i][j]
    if a[i] == b[j]:
        tmp = max(lcs_dp(i-1,j),lcs_dp(i,j-1),lcs_dp(i-1,j-1)+1)
        if states_lcs.get(i) == None:
            states_lcs[i] = {}
            states_lcs[i][j] = tmp
        elif states_lcs.get(i).get(j) == None:
            states_lcs[i][j] = tmp
        else:
            states_lcs[i][j] = tmp
        return states_lcs[i][j]
    else:
        tmp = max(lcs_dp(i-1,j),lcs_dp(i,j-1),lcs_dp(i-1,j-1))
        if states_lcs.get(i) == None:
            states_lcs[i] = {}
            states_lcs[i][j] = tmp
        elif states_lcs.get(i).get(j) == None:
            states_lcs[i][j] = tmp
        else:
            states_lcs[i][j] = tmp
        return states_lcs[i][j]
print("最长公共子串长度，动态规划法：%d" % lcs_dp(5,5))

##莱文斯坦距离的回溯解法
minDist = None
def lvst_huisu(i,j,dist):
    if i == m or j == n:
        global minDist
        if i < m:
            dist += (m-i)
        if j < n:
            dist += (n-j)
        if minDist == None:
            minDist = dist
        elif dist < minDist:
            minDist = dist
        return
    if a[i] == b[j]:
        lvst_huisu(i+1,j+1,dist)
    else:
        lvst_huisu(i+1,j,dist+1)
        lvst_huisu(i,j+1,dist+1)
        lvst_huisu(i+1,j+1,dist+1)
lvst_huisu(0,0,0)
print("莱文斯坦距离，回溯法：%d" % minDist)
##莱文斯坦距离的动态规划解法
states_lvst = {0:{0:0}}
def lvst_dp(i,j):
    if i == 0 and j == 0:
        return states_lvst[0][0]
    if i < 0:
        return m
    if j < 0:
        return n
    if states_lvst.get(i) != None and states_lvst.get(i).get(j) != None:
        return states_lvst[i][j]
    if a[i] == b[j]:
        tmp = min(lvst_dp(i-1,j)+1,lvst_dp(i,j-1)+1,lvst_dp(i-1,j-1))
        if states_lvst.get(i) == None:
            states_lvst[i] = {}
            states_lvst[i][j] = tmp
        elif states_lvst.get(i).get(j) == None:
            states_lvst[i][j] = tmp
        else:
            states_lvst[i][j] = tmp
        return states_lvst[i][j]
    else:
        tmp = min(lvst_dp(i-1,j)+1,lvst_dp(i,j-1)+1,lvst_dp(i-1,j-1)+1)
        if states_lvst.get(i) == None:
            states_lvst[i] = {}
            states_lvst[i][j] = tmp
        elif states_lvst.get(i).get(j) == None:
            states_lvst[i][j] = tmp
        else:
            states_lvst[i][j] = tmp
        return states_lvst[i][j]
print("莱文斯坦距离，动态规划法：%d" % lvst_dp(5,5))


##最长递增子序列
input_arr = [2,9,3,6,5,1,7]
states_las = {0:[2]}
def las_dp(i):
    if states_las.get(i) != None:
        return states_las[i]
    prev_arr = las_dp(i-1)
    len_prev = len(prev_arr)
    if input_arr[i] < prev_arr[len_prev-1] and input_arr[i] >= prev_arr[len_prev-2]:
        tmp_arr = [prev_arr[k] for k in range(len_prev-1)]
        tmp_arr.append(input_arr[i])
        states_las[i] = tmp_arr
        return states_las[i]
    elif input_arr[i] >= prev_arr[len_prev-1]:
        tmp_arr = [prev_arr[k] for k in range(len_prev)]
        tmp_arr.append(input_arr[i])
        states_las[i] = tmp_arr
        return states_las[i]
    else:
        tmp_arr = [prev_arr[k] for k in range(len_prev)]
        states_las[i] = tmp_arr
        return states_las[i]
print("最长递增子序列，动态规划解法：",end="")
print(las_dp(6))
print(las_dp(5))
print(las_dp(4))
print(las_dp(3))
print(las_dp(2))
print(las_dp(1))
print(las_dp(0))
