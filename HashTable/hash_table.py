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

如何设计散列函数：散列函数设计的好坏，决定了散列冲突的概率大小，也直接决定了散列表的性能。
首先，散列函数的设计不能太复杂；其次，散列函数生成的值要尽可能随机并且分布均匀。

装载因子超过某个阈值，需要进行扩容。
如何高效地扩容：为了解决一次性扩容耗时过多的情况，我们可以将扩容操作穿插在插入操作的过程中，分批完成。当有新数据要插入时，我们将新数据插入新散列表中，并且从老的散列表中拿出一个数据放入到新散列表，每次插入一个数据到散列表，都重复上述的过程，经过多次插入操作后，老的散列表中的数据就一点点全部搬移到新散列表中了。这期间的查询操作，为了兼容新、老散列表中的数据，先从新散列表中查找，如果没有找到，再去老的散列表中查找。

如何选择冲突解决方法：两种方法的优势和劣势，各自适用的场景。
开放寻址法：散列表数据都存储在数组中，可以有效利用CPU缓存加快查询速度，而且序列化起来比较简单。删除数据的时候比较麻烦，需要特殊标记已经删除掉的数据，而且装载因子的上限不能太大，导致更浪费内存空间。

"""

##


if __name__ == "__main__":
    pass
