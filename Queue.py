# -*- coding: utf-8 -*-
from __future__ import print_function
from List import LNode,LinkedList

"""
队列：
"""

##链式队列的实现
class LQueue(object):
    def __init__(self):
        self.lst = LinkedList()

    def dequeue(self):
        tmp = self.lst.head
        self.lst.delete_node(None,self.lst.head)
        return tmp

    def enqueue(self, data):
        self.lst.append(LNode(data))





if __name__ == "__main__":
    ##测试链式队列
    que = LQueue()
    for i in range(5):
        que.enqueue(i)
    que.lst.print()
    for i in range(2):
        print(que.dequeue().data)
    que.lst.print()
    for i in range(5):
        print(que.dequeue())
    for i in range(10):
        que.enqueue(i)
    que.lst.print()
