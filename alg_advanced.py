# -*- coding: utf-8 -*-
from __future__ import print_function ##使用python3中给end参数赋空(值)的方式实现输出不换行
import Queue

##拓扑排序：有向无环图
##Kahn实现拓扑排序：借助队列将顶点顺序输出，迭代时将入度为0的顶点入队，某顶点出队时，将其可达顶点的入度都减1，如果顶点入度变为0就入队
graph = {0:[1,3],2:[4,0,1],1:[3],3:[4],4:[]}
def topoSort_Kahn(n):
    #统计每个顶点的入度
    inDegree = {k:0 for k in range(5)}
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

topoSort_Kahn(5)

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
    visited = {k:False for k in range(num_vertex)}
    for v in range(num_vertex):
        if not visited[v]:
            visited[v] = True
            dfs(v,visited,inverse)
    print("")

topoSort_DFS(5,inverse_graph)

##拓扑排序：有向无环图
##BFS实现拓扑排序：从入度为0的顶点开始，进行BFS
def topoSort_BFS(n):
    #统计每个顶点的入度
    inDegree = {k:0 for k in range(n)}
    for k,v in graph.items():
        for i in v:
            inDegree[i] += 1
    #记录顶点是否打印
    visited = {k:False for k in range(n)}
    #队列用于逐层遍历
    q = Queue.Queue()
    for k,v in inDegree.items():
        if v == 0:
            q.put(k)
    while not q.empty():
        vertex = q.get()
        if visited[vertex]:
            continue
        if len(graph.get(vertex)) == 0 and not q.empty():
            continue
        for tv in graph.get(vertex):
            q.put(tv)
        visited[vertex] = True
        print(vertex,end="->")
    print("end")

topoSort_BFS(5)

