# -*- coding: utf-8 -*-

"""
breadthOrder:
               2
            /     \
           1       4
          /  \    /  \
         3    5  7

dequeue<-- Queue <--enqueue                   print
2
                                                2
1 4
                                                1
4 3 5
                                                4
3 5 7
                                                3
5 7
                                                5
7
                                                7
empty 
"""
from queue import Queue

def breadthOrder(node):
    q = Queue()
    q.put(node)
    while not q.empty():
        t = q.get()
        print('{}'.format(t.data))
        if t.left != None:
            q.put(t.left)
        if t.right != None:
            q.put(t.right)

