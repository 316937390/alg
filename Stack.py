# -*- coding: utf-8 -*-
from __future__ import print_function
from List import LNode,LinkedList

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