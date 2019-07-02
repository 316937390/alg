# -*- coding: utf-8 -*-
from __future__ import print_function
from List import LNode,LinkedList

"""
队列：也是一种操作受限的线性表，先进先出。用数组实现的队列叫作顺序队列，用链表实现的队列叫作链式队列。
队列的基本操作：入队、出队，需要两个指针，分别指向队头和队尾
顺序队列在出队时可以不用搬移数据，如果没有空闲空间了，只需要在入队时，集中触发一次数据的搬移操作：重点是复杂度分析
循环队列：避免了数据搬移，但是需要确定好队列空和队列满的判定条件
队列空：head == tail
队列满：(tail+1)%n == head（循环队列会浪费一个存储空间）
阻塞队列和并发队列：

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
