# -*- coding: utf-8 -*-
from __future__ import print_function

"""
如何理解“图”：图是一种非线性表数据结构，图中的元素称为顶点（vertex），顶点之间建立的连接关系叫做边（edge），跟顶点相连接的边的条数叫做顶点的度（degree）。
边有方向的图叫做有向图，边没有方向的图叫做无向图。
在有向图中，把度分为入度（in-degree）和出度（out-degree）。
顶点的入度表示有多少条边指向这个顶点，顶点的出度表示有多少条边是以这个顶点为起点指向其他顶点的。
带权图（weighted graph），在带权图中每条边都有一个权重（weight）。

1、邻接矩阵存储方法
邻接矩阵（Adjacency Matrix）的底层依赖一个二维数组。
    用邻接矩阵来表示一个图，虽然简单、直观，但是比较浪费存储空间。无向图的二维数组中，因为以对角线为轴对称，我们只需要利用一半就够了，另外一半白白浪费了。
    另外，如果是稀疏图(Sparse Matrix)，即顶点很多，但是每个顶点的边并不多，那邻接矩阵的存储方法就更加浪费空间了。
    邻接矩阵的存储方法也有优点，首先，邻接矩阵基于数组，在获取两个顶点的关系时，非常高效。其次，可以将图的运算转换成矩阵之间的运算，比如求解最短路径的Floyd-Warshall算法，就是利用矩阵循环相乘若干次得到结果。
2、邻接表存储方法
邻接表（Adjacency List）每个顶点对应一条链表，链表中存储的是与这个顶点相连接的其他顶点。邻接表存储起来比较节省空间。
    比起邻接矩阵的存储方式，在邻接表中查询两个顶点之间的关系就没有那么高效了，
    邻接表类似散列表，可以将链表换成其他更加高效的数据结构，比如红黑树、跳表、散列表。

"""


def RoundTripMatrix(mat):
	row = len(mat)
	col = len(mat[0])
	for i in range(row):
		if i % 2 == 0:
			for j in range(col):
				print('{} '.format(mat[i][j]),end='')
		else:
			for j in range(col):
				print('{} '.format(mat[i][col-1-j]),end='')

def RoundTripMatrix_c(mat):
	row = len(mat)
	col = len(mat[0])
	for i in range(col):
		if i % 2 == 0:
			for j in range(row):
				print('{} '.format(mat[j][i]),end='')
		else:
			for j in range(row):
				print('{} '.format(mat[row-1-j][i]),end='')

if __name__ == "__main__":
    # 矩阵的回文打印
    mat = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    ## 预期输出为: 1 2 3 6 5 4 7 8 9 12 11 10
    RoundTripMatrix(mat)
    print('')
    ## 预期输出为: 1 4 7 10 11 8 5 2 3 6 9 12
    RoundTripMatrix_c(mat)