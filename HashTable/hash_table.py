# -*- coding: utf-8 -*-
from __future__ import print_function

"""
散列表：散列表用的是数组支持按照下标随机访问数据的特性，所以散列表其实就是数组的一种扩展，由数组演化而来。散列表两个核心问题是散列函数的设计和散列冲突的解决。
键/关键字、散列函数、散列值
散列函数的基本要求：
    1、散列值是一个非负整数
    2、如果key1 == key2，那么hash(key1) == hash(key2)
    3、如果key1 != key2，那么hash(key1) != hash(key2)
散列冲突：开放寻址法、链表法
1、开放寻址法(open addressing)：如果出现了散列冲突，就重新探测一个空闲位置，将其插入。
    “线性探测”，“二次探测”，“双重散列”
2、链表法(chaining)：在散列表中，每个“桶”（bucket）或者“槽”（slot）会对应一条链表，所有散列值相同的元素都放到相同槽位对应的链表中。
装载因子(load factor)：装载因子 = 散列表中的元素个数 / 散列表的长度，装载因子越大，说明空闲位置越少，冲突越多，散列表的性能会下降。一般情况下，我们会尽可能保证散列表中有一定比例的空闲槽位，用装载因子来表示空位的多少。

如何设计散列函数：散列函数设计的好坏，决定了散列冲突的概率大小，也直接决定了散列表的性能。
首先，散列函数的设计不能太复杂；其次，散列函数生成的值要尽可能随机并且分布均匀。

装载因子超过某个阈值，需要进行扩容。
如何高效地扩容：为了解决一次性扩容耗时过多的情况，我们可以将扩容操作穿插在插入操作的过程中，分批完成。当有新数据要插入时，我们将新数据插入新散列表中，并且从老的散列表中拿出一个数据放入到新散列表，每次插入一个数据到散列表，都重复上述的过程，经过多次插入操作后，老的散列表中的数据就一点点全部搬移到新散列表中了。这期间的查询操作，为了兼容新、老散列表中的数据，先从新散列表中查找，如果没有找到，再去老的散列表中查找。

如何选择冲突解决方法：两种方法的优势和劣势，各自适用的场景。
开放寻址法：散列表数据都存储在数组中，可以有效利用CPU缓存加快查询速度，而且序列化起来比较简单。删除数据的时候比较麻烦，需要特殊标记已经删除掉的数据，而且装载因子的上限不能太大，导致更浪费内存空间。当数据量比较小、装载因子小的时候，适合采用开放寻址法。
链表法：链表的结点可以在需要时再创建，对内存的利用率较高；对大装载因子的容忍度较高；因为链表中的结点是零散分布在内存中的，不是连续的，对CPU缓存不友好；可以将链表改造为其他高效的动态数据结构，如跳表、红黑树等，可以有效避免散列碰撞攻击。当存储大对象、大数据量时，适合采用链表法，它更加灵活，支持更多的优化策略。

如何实现一个工业级散列表：
1、设计合适的散列函数
2、定义装载因子阈值，并且设计动态扩容策略
3、选择合适的散列冲突解决方法

散列表中的数据都是通过散列函数打乱之后无规律存储的，即它无法支持按照某种顺序快速遍历数据，散列表是动态数据结构，支持非常高效的插入、删除和查找操作，为了解决按照顺序快速遍历数据的问题，将散列表和链表（或跳表）结合在一起使用。

散列表和链表组合起来使用，实现LRU缓存淘汰算法：
单纯用链表实现的LRU缓存淘汰算法的时间复杂度很高，是O(n)。通过引入散列表，可以将“查找”操作的时间复杂度变为O(1)。
双向链表+散列表中的拉链：前驱和后继指针是为了将结点串在双向链表中，hnext指针是为了将结点串在散列表的拉链中。

Java LinkedHashMap:通过双向链表和散列表这两种数据结构组合实现，“Linked”实际上指的是双向链表，并非指用链表法解决散列冲突。

"""

##散列表+双向链表
class HashNode(object):
    def __init__(self,key=None,value=None):
        self.prev = None
        self.next = None
        self.hnext = None
        self.data = [key,value]

class AHashTable(object):
    def __init__(self,cap=16):
        self.capacity = cap
        self.head = None
        self.tail = None
        self.data = [HashNode()]*cap
        self.number = 0

    def find(self,key):
        hashcode = self.__hashCode(key)
        slot = self.data[hashcode]
        while slot != None:
            if slot.data[0] == key:
                break
            slot = slot.hnext
        if slot == None:
            return None
        #找到key，放到链表尾部
        if self.tail == slot:
            return self.tail
        else:
            if slot.prev != None:
                slot.prev.next = slot.next
            else:
                self.head = slot.next
            slot.next.prev = slot.prev
            self.tail.next = slot
            slot.next = None
            slot.prev = self.tail
            self.tail = slot
            return self.tail

    #func: insert
    #return:  0    直接插入
    #         1    删除后插入
    #         2    更新
    def insert(self,key,value):
        hashcode = self.__hashCode(key)
        slot = self.data[hashcode]
        h_pre = None
        while slot != None:
            if slot.data[0] == key:
                break
            h_pre = slot
            slot = slot.hnext
        if slot == None:
            node = HashNode(key, value)
            h_pre.hnext = node
            if self.number >= self.capacity:
                if self.head == self.tail:
                    self.head = node
                    self.tail = node
                else:
                    self.head.next.prev = None
                    self.head = self.head.next
                    self.tail.next = node
                    node.next = None
                    node.prev = self.tail
                    self.tail = node
                return 1
            else:
                if self.number != 0:
                    self.tail.next = node
                    node.next = None
                    node.prev = self.tail
                    self.tail = node
                else:
                    self.head = node
                    self.tail = node
                self.number += 1
                return 0
        else:
            slot.data[1] = value
            if self.tail == slot:
                return 2
            else:
                if slot.prev != None:
                    slot.prev.next = slot.next
                else:
                    self.head = slot.next
                slot.next.prev = slot.prev
                self.tail.next = slot
                slot.next = None
                slot.prev = self.tail
                self.tail = slot
                return 2

    #func: delete
    #return:  -1   无法找到key
    #         0    成功删除
    def delete(self,key):
        hashcode = self.__hashCode(key)
        slot = self.data[hashcode]
        h_pre = None
        while slot != None:
            if slot.data[0] == key:
                break
            h_pre = slot
            slot = slot.hnext
        if slot == None:
            return -1
        h_pre.hnext = slot.hnext
        if self.head == slot:
            self.head = slot.next
        if self.tail == slot:
            self.tail = slot.prev
        if slot.prev != None:
            slot.prev.next = slot.next
        if slot.next != None:
            slot.next.prev = slot.prev
        self.number -= 1
        return 0

    def __hashCode(self,key):
        return int(key) % self.capacity

    def printAll(self):
        p = self.head
        while p:
            print(p.data,end="->")
            p = p.next
        print("END")

if __name__ == "__main__":
    #测试散列表+双向链表
    ht = AHashTable()
    for i in range(20):
        ht.insert(i,i**2)
    ht.printAll()
    for i in range(10,20,2):
        ht.delete(i)
    ht.printAll()
    for i in range(20):
        print(i,ht.find(i))
        ht.printAll()

