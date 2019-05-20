# -*- coding: utf-8 -*-
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
q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
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
