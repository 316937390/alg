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

二叉查找树(Binary Search Tree)：支持动态数据集合的快速插入、删除、查找操作
二叉查找树要求，在树中的任意一个节点，其左子树的每个节点的值都要小于这个节点的值，而其右子树的每个节点的值都大于这个节点的值。

"""
class TreeNode(object):
    def __init__(self,value=None):
        self.data = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def inOrder(self):
        self.__in_order(self.root)
        print("END")

    def __in_order(self,node):
        if node == None:
            return
        self.__in_order(node.left)
        print(node.data,end=",")
        self.__in_order(node.right)

    def find(self,value):
        p = self.root
        while p:
            if value < p.data:
                p = p.left
            elif value > p.data:
                p = p.right
            else:
                return p
        return None

    def insert(self,value):
        p = self.root
        if p == None:
            self.root = TreeNode(value)
            return self.root
        prev = None
        while p:
            prev = p
            if value <= p.data:
                p = p.left
            else:
                p = p.right
        if value <= prev.data:
            prev.left = TreeNode(value)
            return prev.left
        else:
            prev.right = TreeNode(value)
            return prev.right

    def delete(self,value):
        p = self.root
        pp = None
        while p and p.data != value:
            pp = p
            if value < p.data:
                p = p.left
            elif value > p.data:
                p = p.right
        if p == None:  ##没有找到
            return -1
        ##要删除的节点有两个子节点
        if p.left != None and p.right != None:
            minP = p.right
            minPP = p
            while minP.left:
                minPP = minP
                minP = minP.left
            p.data = minP.data
            p = minP
            pp = minPP
        #删除节点是叶子节点或者仅有一个子节点
        child = None
        if p.left != None:
            child = p.left
        elif p.right != None:
            child = p.right
        else:
            child = None

        if pp == None:
            self.root = child
        elif pp.left == p:
            pp.left = child
        elif pp.right == p:
            pp.right = child

        return 0




if __name__ == "__main__":
    ##测试二叉查找树
    bst = BST()
    arr = [5,3,1,4,8,6,10]
    for i in arr:
        bst.insert(i)
    bst.inOrder()
    print(bst.find(5).data)
    print(bst.find(3).data)
    print(bst.find(10).data)
    print(bst.find(20))
    print(bst.delete(10))
    print(bst.delete(8))
    print(bst.delete(5))
    print(bst.delete(20))
    bst.inOrder()

