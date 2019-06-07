# -*- coding: utf-8 -*-
from __future__ import print_function
import Queue


##AC自动机:多模式串匹配，例如：敏感词过滤
rules = ["samsung,ios","applovin,android,vre","doubleclick","vin,US,HeadBid,v10","ios,vin,JP,HeadBid,v9","mopub,ios,i,US,HeadBid,v10"]
#构建trie树，构建fail指针

