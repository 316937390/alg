# -*- coding: utf-8 -*-
from __future__ import print_function

def generator(k):
    i = 1
    while True:
        yield i ** k  ## yield是关键，可以理解为程序运行到这一行的时候，会从这里暂停，然后跳出到next()函数
        i += 1

gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):  ## 事实上，迭代器是一个有限集合，而生成器则可以成为一个无限集合
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

get_sum(8)

def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i

g_index = index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)
print(g_index)
print(list(g_index))



def is_subsequence(a, b):
    b = iter(b)
    '''
    print(b)

    gen = (i for i in a)
    print(gen)

    for i in gen:
        print(i)

    gen = ((i in b) for i in a)
    print(gen)

    for i in gen:
        print(i)
    '''
    return all(((i in b) for i in a))
print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))


def maxFactor(f, g):
    """
    求解最大公因数
    辗转相除
    """
    assert f >= g
    r = f % g
    while r != 0:
        t = g % r
        g = r
        r = t
    return g

print("max factor:{}".format(maxFactor(546,325)))