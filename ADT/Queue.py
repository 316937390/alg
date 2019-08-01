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
阻塞队列：在队列的基础上增加了阻塞操作，入队和出队操作可以阻塞
并发队列：线程安全的队列
CAS原子操作：compare-and-swap，实现无锁并发队列
实际上，对于大部分资源有限的场景，当没有空闲资源时，基本上都可以通过“队列”来实现请求排队
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

##循环队列
class CircularQueue(object):
    def __init__(self,capacity):
        self.array = [None]*capacity
        self.n = capacity
        self.head = 0
        self.tail = 0

    def dequeue(self):
        if self.head == self.tail:
            return None
        else:
            tmp = self.array[self.head]
            self.head = (self.head+1)%self.n
            return tmp

    def enqueue(self,data):
        if (self.tail+1)%self.n == self.head:
            return False
        else:
            self.array[self.tail] = data
            self.tail = (self.tail+1)%self.n
            return True
    



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
    ##测试循环队列
    cque = CircularQueue(5)
    print(cque.dequeue())
    for i in range(5):
        cque.enqueue(i)
    for i in range(5):
        print(cque.dequeue())
    for i in range(2,20,2):
        cque.enqueue(i)
    for i in range(5):
        print(cque.dequeue())
    print(cque.array)
