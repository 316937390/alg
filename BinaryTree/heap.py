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
    删除堆顶元素：从上往下堆化
    堆化过程是顺着节点所在路径比较交换，堆化的时间复杂度跟树的高度成正比，即O(logn)。
    上述插入、删除的主要逻辑就是堆化，因此往堆中插入一个元素和删除堆顶元素的时间复杂度都是O(logn)。
基于堆实现排序：建堆和排序
建堆过程的时间复杂度是O(n)。
排序过程的时间复杂度是O(nlogn)。
堆排序是原地排序算法，不是稳定的排序算法。
"""
##大顶堆
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
        ##堆化
        while (i>>1) > 0 and self.data[i] > self.data[(i>>1)]:
            tmp = self.data[(i>>1)]
            self.data[(i>>1)] = self.data[i]
            self.data[i] = tmp
            i = (i>>1)
        return True

    def removeMax(self):
        if self.count == 0:
            return False
        self.data[1] = self.data[self.count]
        self.count -= 1
        ##堆化
        self.heapify(1)
        return True

    def heapify(self,i):
        while True:
            maxPos = i
            if i*2 <= self.count and self.data[i] < self.data[i*2]:
                maxPos = i*2
            if i*2+1 <= self.count and self.data[maxPos] < self.data[i*2+1]:
                maxPos = i*2+1
            if maxPos == i:
                break
            tmp = self.data[i]
            self.data[i] = self.data[maxPos]
            self.data[maxPos] = tmp
            i = maxPos

def buildHeap(arr,n):
    i = (n>>1)
    while i >= 1:
        heapify(arr,n,i)
        i -= 1

def heapify(arr,n,i):
    while True:
        maxPos = i
        if i*2 <= n and arr[i] < arr[i*2]:
            maxPos = i*2
        if i*2+1 <= n and arr[maxPos] < arr[i*2+1]:
            maxPos = i*2+1
        if maxPos == i:
            break
        tmp = arr[i]
        arr[i] = arr[maxPos]
        arr[maxPos] = tmp
        i = maxPos


def heapsort(arr,n):
    buildHeap(arr,n)
    k = n
    while k > 1:
        tmp = arr[1]
        arr[1] = arr[k]
        arr[k] = tmp
        k -= 1
        heapify(arr,k,1)


if __name__ == "__main__":
    ##测试堆
    heap = Heap(20)
    for i in range(25):
        heap.insert(i)
    print(heap.data,heap.count)
    heap.removeMax()
    print(heap.data,heap.count)
    ##测试堆排序
    arr = [None]
    for i in range(15):
        arr.append(i)
    buildHeap(arr,15)
    print("buildHeap:",arr)
    arr_1 = [None]
    for i in range(20,0,-1):
        arr_1.append(i)
    print(arr_1)
    heapsort(arr_1,20)
    print("heapsort:",arr_1)
