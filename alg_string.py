# -*- coding: utf-8 -*-
from __future__ import print_function
import Queue


##AC自动机:多模式串匹配，例如：敏感词过滤
rules = ["samsung,ios","applovin,android,vre","doubleclick","vin,US,HeadBid,v10","ios,vin,JP,HeadBid,v9","mopub,ios,i,US,HeadBid,v10","vin,JP","ios,vin,v9","HeadBid,v10","doubleclick,ios,vin,JP,HeadBid,v9"]
#构建trie树，构建fail指针
class AcNode(object):
    def __init__(self,field):
        self.dim = field
        self.isEnd = False
        self.length = -1
        self.fail = None
        self.AcNodes = {}

    def isRoot(self):
        return self.dim == "/"

class AcTrie(object):
    def __init__(self):
        self.root = AcNode("/")

    def insert(self,rule):
        p = self.root
        fields = rule.split(",")
        leng = 0
        for field in fields:
            leng += 1
            if p.AcNodes.get(field) == None:
                p.AcNodes[field] = AcNode(field)
            p = p.AcNodes[field]
        p.isEnd = True
        p.length = leng

    def buildFailurePointer(self):
        que = Queue.Queue()
        que.put(self.root)
        while not que.empty():
            p = que.get()
            for k,v in p.AcNodes.items():
                if p.isRoot():
                    p.AcNodes[k].fail = self.root
                else:
                    q = p.fail
                    while q != None:
                        qc = q.AcNodes.get(k)
                        if qc != None:
                            p.AcNodes[k].fail = qc
                            break
                        q = q.fail
                    if q == None:
                        p.AcNodes[k].fail = self.root
                que.put(p.AcNodes[k])

    def match(self,input_string):
        print("输入: %s"%(input_string))
        p = self.root
        fields = input_string.split(",")
        for i in range(len(fields)):
            field = fields[i]
            while p.AcNodes.get(field) == None and (not p.isRoot()):
                p = p.fail
            if p.isRoot() and p.AcNodes.get(field) == None:
                continue
            p = p.AcNodes[field]
            tmp = p
            while not tmp.isRoot():
                if tmp.isEnd:
                    print("匹配rule: [%s] 被过滤!"%(",".join(fields[i-tmp.length+1:i+1])))
                tmp = tmp.fail


ac = AcTrie()
for r in rules:
    print("rule: [%s]"%(r))
    ac.insert(r)
ac.buildFailurePointer()
ac.match("doubleclick,ios,vin,JP,HeadBid,v9")



'''
1、单模式串匹配
BF(暴力匹配、朴素匹配) RK(利用hash函数，比较子串和模式串的hash值)
依次检查起始位置为0、1、2、...、n-m且长度为m的n-m+1个子串，看是否与模式串匹配。

BM：按照模式串下标从大到小，倒着匹配。
    坏字符规则：
    好后缀规则：考察 好后缀的后缀子串 是否存在跟 模式串的前缀子串 匹配的

2、多模式串匹配
Trie树：利用字符串之间的公共前缀，将重复的前缀合并在一起（应用示例：搜索关键词提示功能）
'''