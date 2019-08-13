# -*- coding: utf-8 -*-
from __future__ import print_function

"""
树：父节点、子节点、兄弟节点、根节点、叶子节点
高度(Height)：从最底层开始度量
深度(Depth)：从根节点开始度量
层(Level)：深度+1

二叉树(Binary Tree)：每个节点最多有两个“叉”，即最多两个子节点
满二叉树：叶子节点全都在最底层，除了叶子节点外，每个节点都有左右两个子节点。
完全二叉树：叶子节点都在最底下两层，最后一层的叶子节点都靠左排列，并且除了最后一层，其他层的节点个数都要达到最大。

如何存储一颗二叉树：
    基于指针或引用的链式存储法
    基于数组的顺序存储法(一般情况下，为了方便计算，根节点会存储在下标为1的位置)，适合完全二叉树

二叉树的遍历：
前序、中序、后序遍历，表示的是节点与它的左右子树节点遍历打印的先后顺序。
二叉树遍历的时间复杂度是O(n)。

前序遍历的递推公式：
preOrder(r) = print r->preOrder(r->left)->preOrder(r->right)

中序遍历的递推公式：
inOrder(r) = inOrder(r->left)->print r->inOrder(r->right)

后序遍历的递推公式：
postOrder(r) = postOrder(r->left)->postOrder(r->right)->print r

"""



if __name__ == "__main__":
    pass
