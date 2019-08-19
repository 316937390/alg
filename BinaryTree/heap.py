# -*- coding: utf-8 -*-
from __future__ import print_function

"""
堆：是一种特殊的树，需要满足下面两点：
    （1）堆是一棵完全二叉树
    （2）堆中每一个节点的值都必须大于等于（或小于等于）其子树中节点的值
大顶堆
小顶堆
如何实现一个堆：
    存储一个堆：数组
    往堆中插入一个元素：堆化（heapify）
    删除堆顶元素：
"""
##
class Heap(object):
    def __init__(self,capacity):
        self.data = [None]*(capacity+1)
        self.capacity = capacity
        self.count = 0

    def insert(self,value):
        if self.count >= self.capacity:
            return False
        self.count += 1
        self.data[self.count] = value
        i = self.count
        while (i>>1) > 0 and self.data[i] > self.data[(i>>1)]:
            tmp = self.data[(i>>1)]
            self.data[(i>>1)] = self.data[i]
            self.data[i] = tmp
            i = (i>>1)
        return True



if __name__ == "__main__":
    ##测试堆
    heap = Heap(20)
    for i in range(25):
        heap.insert(i)
    print(heap.data)
