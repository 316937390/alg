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



