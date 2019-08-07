# -*- coding: utf-8 -*-
from __future__ import print_function

"""
散列表：散列表用的是数组支持按照下标随机访问数据的特性，所以散列表其实就是数组的一种扩展，由数组演化而来。散列表两个核心问题是散列函数的设计和散列冲突的解决。
键/关键字、散列函数、散列值
散列函数的基本要求：
    1、散列值是一个非负整数
    2、如果key1 == key2，那么hash(key1) == hash(key2)
    3、如果key1 != key2，那么hash(key1) != hash(key2)
散列冲突：开放寻址法、链表法
1、开放寻址法(open addressing)：如果出现了散列冲突，就重新探测一个空闲位置，将其插入。
    “线性探测”，“二次探测”，“双重散列”
2、链表法(chaining)：在散列表中，每个“桶”（bucket）或者“槽”（slot）会对应一条链表，所有散列值相同的元素都放到相同槽位对应的链表中。
装载因子(load factor)：装载因子 = 散列表中的元素个数 / 散列表的长度，装载因子越大，说明空闲位置越少，冲突越多，散列表的性能会下降。一般情况下，我们会尽可能保证散列表中有一定比例的空闲槽位，用装载因子来表示空位的多少。

"""

##


if __name__ == "__main__":
    pass
