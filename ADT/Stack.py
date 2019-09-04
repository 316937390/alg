# -*- coding: utf-8 -*-
from __future__ import print_function
from ADT.List import LNode,LinkedList

"""
栈：是一种操作受限的线性表，只允许在一端插入和删除数据
当某个数据集合只涉及在一端插入和删除数据，并且满足后进先出、先进后出的特性，我们就应该首选“栈”这种数据结构
如何实现一个栈：栈既可以用数组来实现，又可以用链表来实现。用数组实现的栈，叫做顺序栈，用链表实现的栈，叫作链式栈。
栈主要包含两种操作：入栈和出栈，也就是在栈顶插入一个数据和从栈顶删除一个数据。
支持动态扩容的顺序栈：重点是复杂度分析

栈在函数调用中的应用：函数调用栈
栈在表达式求值中的应用：
栈在括号匹配中的应用：
"""

##链式栈的实现
class LStack(object):
    def __init__(self):
        self.lst = LinkedList()

    def top(self):
        return self.lst.head

    def push(self, data):
        self.lst.insert_head(LNode(data))

    def pop(self):
        tmp = self.lst.head
        self.lst.delete_node(None,self.lst.head)
        return tmp

op_pri = {"+":0,"-":0,"*":1,"/":1} #定义运算符的优先级
brackets = {"{":"}","[":"]","(":")"}  #定义匹配的括号

def isOp(op):
    ops = ["+","-","*","/"]
    if op in ops:
        return True
    else:
        return False

def cal(l,r,op):
    if op == "+":
        return int(l)+int(r)
    elif op == "-":
        return int(l)-int(r)
    elif op == "*":
        return int(l)*int(r)
    elif op == "/":
        return int(l)/int(r)

##表达式求值（这里就不校验表达式的合法性了）
def getResFromExp(expression):
    opcode_st = LStack()
    opnum_st = LStack()
    cache = []
    for i in expression:  ##从左到右遍历表达式
        if isOp(i):
            opnum_st.push("".join(cache))
            cache = []
            if opcode_st.top() == None:
                opcode_st.push(i)
            elif op_pri[i] > op_pri[opcode_st.top().data]:
                opcode_st.push(i)
            else:
                while op_pri[i] <= op_pri[opcode_st.top().data]:
                    op = opcode_st.pop().data
                    r_val = opnum_st.pop().data
                    l_val = opnum_st.pop().data
                    res = cal(l_val, r_val, op)
                    opnum_st.push(str(res))
                    if opcode_st.top() == None:
                        opcode_st.push(i)
                        break
                if op_pri[i] > op_pri[opcode_st.top().data]:
                    opcode_st.push(i)
        else:
            cache.append(i)
    if len(cache) != 0:
        opnum_st.push("".join(cache))
    op = opcode_st.pop().data
    r_val = opnum_st.pop().data
    l_val = opnum_st.pop().data
    res = cal(l_val, r_val, op)
    print("%s = %d" % (expression, res))
    #opnum_st.lst.print()
    #opcode_st.lst.print()


##检查字符串中括号匹配是否合法
def match_brackets(str_input):
    stack = LStack()
    for i in str_input: #从左到右遍历字符串
        if i in brackets.keys():
            stack.push(i)
        elif i in brackets.values():
            tmp = stack.pop()
            if tmp == None:
                return False
            elif brackets[tmp.data] != i:
                return False
            else:
                continue
        else:
            continue
    if stack.top() != None:
        return False
    else:
        return True


if __name__ == "__main__":
    ##测试栈的操作
    stack = LStack()
    for i in range(10):
        stack.push(i)
    stack.lst.print()
    for i in range(20):
        print(stack.pop())
    stack.lst.print()
    ##表达式求值
    expr = "3-3*3*1*1*7-11"
    getResFromExp(expr)
    ##括号匹配(){}[]
    str = "[[[{{((x)y)z}a}v]b]c]"
    #str = "[[[{{((x)y)z}a}vb]c]"
    #str = "[[[{((x)y)z}a}v]b]c]"
    #str = "[[[{{{((x]y)z}a}v]b]c]"
    if match_brackets(str):
        print("\"%s\" is valid" % (str))
    else:
        print("\"%s\" is not valid!!!" % (str))
