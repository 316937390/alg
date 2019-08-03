# -*- coding: utf-8 -*-
from __future__ import print_function
import random

"""
跳表：一种动态数据结构，可以支持快速的插入、删除、查找操作。Redis中的有序集合（Sorted Set）就是用跳表实现的。
链表+多级索引的结构就是跳表。
跳表查询的时间复杂度：
    最高级的索引有2个节点，如果包含原始链表这一层，则整个跳表的高度就是logn，在跳表中查询某个数据时，每一层都要遍历3个节点，那么在跳表中查询任意数据的时间复杂度就是O(logn)。
    换句话说，我们基于单链表实现了“二分查找”。
跳表的空间复杂度：
    比起单纯的单链表，跳表需要存储多级索引，肯定需要消耗更多的存储空间，空间复杂度是O(n)。
    在实际软件开发中，原始链表存储的可能是很大的对象，而索引节点只需要存储关键值和几个指针，并不需要存储对象，因此当对象比索引节点大很多时，那么索引占用的额外空间就可以忽略了。
跳表的插入和删除操作：
    插入、删除的时间复杂度都是O(logn)
跳表索引的动态更新：
    跳表通过随机函数来维护“平衡性”
    插入数据时，通过一个随机函数，来决定同时将这个数据插入到部分索引层中。
    随机函数的选择很有讲究，从概率上讲，能够保证跳表索引大小和数据大小的平衡，不至于性能过度退化。
注：跳表比较适合按照区间查找数据的操作
"""

##跳表的一种实现方法：跳表中存储的是正整数，并且存储的是不重复的
MAX_LEVEL = 5
class Node(object):
    def __init__(self):
        self.data = -1
        self.forwards = [None] * MAX_LEVEL
        self.maxLevel = 0


class SkipList(object):
    def __init__(self):
        self.head = Node()
        self.levelCount = 1

    def randomLevel(self):
        level = 1
        for i in range(1,MAX_LEVEL,1):
            if random.randint(0,100) % 2 == 1:
                level += 1
        return level

    def find(self,value):
        p = self.head
        for i in range(self.levelCount):
            while p.forwards[self.levelCount-1-i] != None and p.forwards[self.levelCount-1-i].data < value:
                p = p.forwards[self.levelCount-1-i]
        if p.forwards[0] != None and p.forwards[0].data == value:
            return p.forwards[0]
        else:
            return None

    def find_last_less(self,value):
        p = self.head
        for i in range(self.levelCount):
            while p.forwards[self.levelCount-1-i] != None and p.forwards[self.levelCount-1-i].data < value:
                p = p.forwards[self.levelCount-1-i]
        if p != self.head:
            return p
        else:
            return None

    def insert(self,value):
        level = self.randomLevel()
        newNode = Node()
        newNode.data = value
        newNode.maxLevel = level
        update = [Node()]*level
        for i in range(level):
            update[i] = self.head
        #record every level largest value which smaller than insert value in update[]
        p = self.head
        for i in range(level):
            while p.forwards[level-1-i] != None and p.forwards[level-1-i].data < value:
                p = p.forwards[level-1-i]
            #use update save node in search path
            update[level-1-i] = p

        #in search path node next node become new node forwords(next)
        for i in range(level):
            newNode.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = newNode

        #update node hight
        if self.levelCount < level:
            self.levelCount = level


    def delete(self,value):
        update = [Node()]*self.levelCount
        p = self.head
        for i in range(self.levelCount):
            while p.forwards[self.levelCount-1-i] != None and p.forwards[self.levelCount-1-i].data < value:
                p = p.forwards[self.levelCount-1-i]
            update[self.levelCount-1-i] = p
        if p.forwards[0] != None and p.forwards[0].data == value:
            for i in range(self.levelCount):
                if update[self.levelCount-1-i].forwards[self.levelCount-1-i] != None and update[self.levelCount-1-i].forwards[self.levelCount-1-i].data == value:
                    update[self.levelCount-1-i].forwards[self.levelCount-1-i] = update[self.levelCount-1-i].forwards[self.levelCount-1-i].forwards[self.levelCount-1-i]

    def printAll(self):
        p = self.head
        lst = []
        while p.forwards[0] != None:
            lst.append(str(p.forwards[0].data))
            p = p.forwards[0]
        print("->".join(lst))


if __name__ == "__main__":
    #测试跳表
    skiplist = SkipList()
    ##插入
    skiplist.insert(10)
    skiplist.insert(9)
    skiplist.insert(1)
    skiplist.insert(4)
    skiplist.printAll()
    ##删除
    skiplist.delete(9)
    skiplist.delete(30)
    skiplist.delete(1)
    skiplist.delete(10)
    skiplist.delete(4)
    skiplist.printAll()
    ##查找
    for i in range(0,1000,2):
        skiplist.insert(i)
    for i in range(100,200,1):
        ret = skiplist.find(i)
        if ret != None:
            print("    find: ",ret.data)
        else:
            print("not find: ",i)
    #区间查找
    p = skiplist.find_last_less(789)
    while p != None:
        if p.forwards[0] != None and p.forwards[0].data < 800:
            print(p.forwards[0].data,end=",")
        p = p.forwards[0]
    p = skiplist.find_last_less(2000)
    while p != None:
        if p.forwards[0] != None and p.forwards[0].data < 2800:
            print(p.forwards[0].data,end=",")
        p = p.forwards[0]
    skiplist = SkipList()
    p = skiplist.find_last_less(5)
    while p != None:
        if p.forwards[0] != None and p.forwards[0].data < 10:
            print(p.forwards[0].data,end=",")
        p = p.forwards[0]

