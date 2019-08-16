# -*- coding: utf-8 -*-
from __future__ import print_function

"""
平衡二叉查找树：二叉查找树中任意一个节点的左右子树的高度相差不能大于1。
    AVL树
解决普通二叉查找树在频繁的插入、删除等动态更新的情况下，出现时间复杂度退化的问题。
平衡二叉查找树中“平衡”的意思，其实就是让整棵树左右看起来比较“对称”、比较“平衡”，不要出现左子树很高、右子树很矮的情况。这样就能让整棵树的高度相对来说低一些，相应的插入、删除、查找等操作的效率高一些。

红黑树：一种不严格的平衡二叉查找树，是“近似平衡”的。
    根节点是黑色的
    每个叶子节点都是黑色的空节点（不存储数据），主要是为了简化红黑树的代码实现
    任何相邻的节点都不能同时为红色
    每个节点，从该节点到达其可达叶子节点的所有路径，都包含相同数目的黑色节点

"""


if __name__ == "__main__":
    pass
