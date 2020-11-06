# -*- coding: utf-8 -*-

import stack

def preOrder(node):
    stack = stack.stack()
    stack.push(node)
    while not stack.empty():
        top = stack.pop()
        print('{}'.format(top.data))
        if top.right != None:
            stack.push(top.right)
        if top.left != None:
            stack.push(top.left)

"""
preOrder:
               2
            /     \
           1       4
          /  \    /  \
         3    5  7

stack                   print
2 <--                       
                            2
4 1 <--
                            1
4 5 3 <--
                            3
4 5 <--
                            5
4 <--
                            4
7 <--
                            7
<--
""" 

def inOrder(node):
  stack = stack.stack()
  stack.push(node)
  finished = False
  while not stack.empty():
    top = stack.top()
    if finished:
      print('{}'.format(top.data))
      stack.pop()
      if top.right != None:
        stack.push(top.right)
        finished = False
    elif top.left != None:
      stack.push(top.left)
    else:
      print('{}'.format(top.data))
      if top.right != None:
        stack.push(top.right)
        finished = False
      else:
        finished = True # leaf
        stack.pop()
      

"""
inOrder
               2
            /     \
           1       4
          /  \    /  \
         3    5  7

stack                   print
2 <--
2 1 <--
2 1 3 <--
                          3
2 1 <--                     true
                          1
2 5 <--                     false  
                          5
2 <--                       true
                          2
4 <--                       false
4 7 <--                     
                          7
4 <--                       true
                          4
<--
"""


def postOrder(node):
  stack = stack.stack()
  stack.push(node)
  while not stack.empty():
    top = stack.top()
    if top.left != None:
      stack.push(top.left)
    elif top.right != None:
      stack.push(top.right)
    else:
      print('{}'.format(top.data))
      stack.pop()
    pass









"""
postOrder
               2
            /     \
           1       4
          /  \    /  \
         3    5  7

stack                   print
2 <--
2 1 <--
2 1 3 <--
                          3
2 1 5 <--                  
                          5
2 1 <--                    
                          1
2 4 <--                      
2 4 7 <--
                          7
2 4 <--                      
                          4
2 <--                        
                          2
"""
