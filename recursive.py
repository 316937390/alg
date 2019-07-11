# -*- coding: utf-8 -*-
from __future__ import print_function
from Stack import LStack


"""
如何理解“递归”
递归需要满足的三个条件：
1、一个问题的解可以分解为几个子问题的解
2、原问题和分解后的子问题，除了数据规模不同，求解思路完全一样
3、存在递归终止条件
递推公式，终止条件
递归代码要警惕堆栈溢出：限制递归调用的最大深度。
递归代码要警惕重复计算：可以通过一个数据结构（比如哈希表）来保存已经求解过的结果，当递归调用时，先看下是否已经求解过了，如果是，则直接从哈希表中取值返回。
递归代码函数调用耗时多、空间复杂度高。
怎么将递归代码改写为非递归代码：如果我们自己实现栈，手动模拟入栈、出栈过程，这样任何递归代码都可以改写成看上去不是递归代码的样子，~~wow,magic~~
"""

##假设有n个台阶，每次可以跨1个或者2个台阶，请问这n个台阶有多少种走法？
hash_map = {}
def stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if hash_map.get(n) != None:
        return hash_map[n]
    ret = stairs(n-1)+stairs(n-2)
    hash_map[n] = ret
    return ret

def stairs_v2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    stack = LStack()
    stack.push(n-2)
    stack.push(n-1)
    sum = 0
    while stack.top() != None:
        cur = stack.pop().data
        if cur == 1:
            sum += 1
        elif cur == 2:
            sum += 2
        else:
            stack.push(cur-2)
            stack.push(cur-1)
    return sum


if __name__ == "__main__":
    print(stairs(1))
    print(stairs(2))
    print(stairs(3))
    print(stairs(30))
    print(stairs_v2(1))
    print(stairs_v2(2))
    print(stairs_v2(3))
    print(stairs_v2(30))
