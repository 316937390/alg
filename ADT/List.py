# -*- coding: utf-8 -*-
from __future__ import print_function


##链表：通过指针将零散的内存块串联起来使用
"""
单链表、双向链表、循环链表
在链表中插入和删除操作非常快速，只需要考虑相邻结点的指针改变，因此对应的时间复杂度为O(1)
在链表中随机访问的性能差，需要O(n)的时间复杂度
循环链表特别适用于数据具有环形结构特点的场景，比如约瑟夫问题
双向链表，在实际开发中更加常用，可以支持O(1)时间复杂度的情况下找到前驱结点
删除操作：删除值等于某个给定值的结点；删除给定指针指向的结点；
插入操作：在某个指定结点前面插入
双向循环链表
空间换时间、时间换空间
数组vs链表性能比较：插入/删除、随机访问
典型应用：LRU缓存淘汰算法
维护一个有序链表，越靠近尾部的结点是越早之前访问的（可以考虑淘汰）
从链表头开始顺序遍历，如果数据在链表中，则将对应的结点从原来位置删除，插入到链表头部；
如果数据不在链表中，若此时缓存未满，则将新数据结点插入到链表头部，若此时缓存已满，则将链表尾结点删除，将新数据结点插入到链表头部
"""
##单链表
class LNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head(self,node):
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def delete_node(self,prev,node):
        if node == None:
            return
        if prev != None:
            prev.next = node.next
        else:
            self.head = node.next
        self.length -= 1

    def append(self,node):
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data,end="->")
            tmp = tmp.next
        print("null")

    def reverse(self,begin,end):
        prev = None
        cur = begin
        while prev != end and cur:
            n_next = cur.next
            cur.next = prev
            prev = cur
            cur = n_next

##LRU缓存
class LRU_Cache(object):
    def __init__(self,capacity):
        self.lst = LinkedList()
        self.capacity = capacity

    def find(self,data):
        tmp = self.lst.head
        prev = None
        tail_prev = None
        while tmp:
            if tmp.data == data:
                break
            tail_prev = prev
            prev = tmp
            tmp = tmp.next
        if tmp == None: #not found
            if self.lst.length < self.capacity:
                self.lst.insert_head(LNode(data))
            else:
                self.lst.delete_node(tail_prev,prev)
                self.lst.insert_head(LNode(data))
        else:
            if prev:
                self.lst.delete_node(prev,tmp)
                self.lst.insert_head(tmp)
        return self.lst.head.data

##判断是否为回文串，单链表存储字符串
def verify_round_string(input_str):
    lst = LinkedList()
    for i in range(len(input_str)):
        lst.append(LNode(input_str[i]))
    lst.print()
    prev_node = None
    tmp_slow = lst.head #链表中间结点
    tmp_fast = lst.head
    while tmp_fast and tmp_fast.next :
        prev_node = tmp_slow
        tmp_slow = tmp_slow.next
        tmp_fast = tmp_fast.next.next
    if tmp_fast == None:  ##even
        lst.reverse(lst.head,prev_node) #反转
        while prev_node and tmp_slow :
            if prev_node.data == tmp_slow.data:
                prev_node = prev_node.next
                tmp_slow = tmp_slow.next
            else:
                print("不是回文串")
                break
    elif tmp_fast.next == None: ##odd
        tmp_slow = tmp_slow.next
        lst.reverse(lst.head,prev_node) #反转
        while prev_node and tmp_slow :
            if prev_node.data == tmp_slow.data:
                prev_node = prev_node.next
                tmp_slow = tmp_slow.next
            else:
                print("不是回文串")
                break

##两个有序链表合并
def merge_sorted_list(lst_a, lst_b):
    cur_a = lst_a.head
    cur_b = lst_b.head
    base = None #用于记录merge_list
    if cur_a == None: #a为空
        return lst_b
    elif cur_b == None: #b为空
        return lst_a
    while cur_a and cur_b:
        if cur_a.data <= cur_b.data:
            if base == None:
                base = cur_a
                cur_a = cur_a.next
            elif base.next == cur_a:
                base = cur_a
                cur_a = cur_a.next
            elif base.next == cur_b:
                next_a = cur_a.next
                cur_a.next = cur_b
                base.next = cur_a
                cur_a = next_a
                base = base.next
        else:
            if base == None:
                base = cur_b
                cur_b = cur_b.next
            elif base.next == cur_a:
                next_b = cur_b.next
                cur_b.next = cur_a
                base.next = cur_b
                cur_b = next_b
                base = base.next
            elif base.next == cur_b:
                base = cur_b
                cur_b = cur_b.next
    if cur_a == None:
        if base.next == cur_a:
            base.next = cur_b
            return lst_a
        elif base.next == cur_b:
            return lst_b
    elif cur_b == None:
        if base.next == cur_b:
            base.next = cur_a
            return lst_b
        elif base.next == cur_a:
            return lst_a


if __name__ == "__main__":
    ##测试两个有序链表合并
    print("测试两个有序链表合并")
    a = [1,3,5,7]
    b = [0,4,8,12]
    a = [1,4,8,15]
    b = [0,4,8,12]
    a = []
    b = [0,4,8,12]
    a = [0,2,2,2]
    b = [1,2,2,2]
    a_list = LinkedList()
    b_list = LinkedList()
    for i in a:
        a_list.append(LNode(i))
    for j in b:
        b_list.append(LNode(j))

    a_list.print()
    b_list.print()
    m_list = merge_sorted_list(a_list, b_list)
    m_list.print()

    ##测试单链表反转

    ##链表中环的检测

    ##删除链表倒数第n个结点


    ##测试判断回文串
    print("测试判断回文串")
    verify_round_string("a")
    verify_round_string("ab")
    verify_round_string("aa")
    verify_round_string("abaa")
    verify_round_string("abba")
    verify_round_string("abbaa")
    verify_round_string("abbba")
    verify_round_string("")

    ##测试LRU缓存淘汰算法的链表实现
    print("测试LRU缓存淘汰算法")
    cache = LRU_Cache(1)
    print(cache.find(23))
    cache.lst.print()
    print(cache.find(21))
    cache.lst.print()
    print(cache.find(25))
    cache.lst.print()

    cache = LRU_Cache(2)
    print(cache.find(23))
    cache.lst.print()
    print(cache.find(21))
    cache.lst.print()
    print(cache.find(23))
    cache.lst.print()
    print(cache.find(25))
    cache.lst.print()
    print(cache.find(25))
    cache.lst.print()
    print(cache.find(26))
    cache.lst.print()
    print(cache.find(25))
    cache.lst.print()

    cache = LRU_Cache(10)
    for i in range(20):
        print(cache.find(i))
    cache.lst.print()
    for i in range(10):
        print(cache.find(i))
    cache.lst.print()
