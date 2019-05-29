# -*- coding: utf-8 -*-
from __future__ import print_function ##使用python3中给end参数赋空(值)的方式实现输出不换行
import Queue

##拓扑排序：有向无环图
##Kahn实现拓扑排序：借助队列将顶点顺序输出，迭代时将入度为0的顶点入队，某顶点出队时，将其可达顶点的入度都减1，如果顶点入度变为0就入队
graph = {0:[1,3],2:[4,0,1],1:[3],3:[4],4:[]}
def topoSort_Kahn():
    #统计每个顶点的入度
    inDegree = {0:0,1:0,2:0,3:0,4:0}
    for k,v in graph.items():
        for i in v:
            inDegree[i] += 1
    print("顶点的入度：",end="")
    print(inDegree)
    q = Queue.Queue()
    for k,v in inDegree.items():
        if v == 0:
            q.put(k)
    while not q.empty():
        vertex = q.get()
        print(vertex,end="->")
        for tv in graph.get(vertex):
            inDegree[tv] -= 1
            if inDegree[tv] == 0:
                q.put(tv)
    print("end")

topoSort_Kahn()

##拓扑排序：有向无环图
##DFS实现拓扑排序：首先构造逆邻接表，然后进行深度优先遍历
inverse_graph = {0:[],1:[],2:[],3:[],4:[]}
for k,v in graph.items():
    for i in v:
        inverse_graph[i].append(k)
print("逆邻接表:",end="")
print(inverse_graph)
print("邻接表:",end="")
print(graph)
def dfs(v,visited,inverse):
    for i in inverse[v]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i,visited,inverse)
    print("->%d" % v,end="")

def topoSort_DFS(num_vertex,inverse):
    visited = {0:False,1:False,2:False,3:False,4:False}
    for v in range(num_vertex):
        if not visited[v]:
            visited[v] = True
            dfs(v,visited,inverse)
    print("")

topoSort_DFS(5,inverse_graph)

