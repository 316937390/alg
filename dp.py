# -*- coding: utf-8 -*-

b_weight = 20 #背包重量
item_w = {0:3,1:5,2:10,3:8,4:1,5:6} # key:物品 value:weight
item_m = {0:6,1:20,2:5,3:7,4:3,5:4} # key:物品 value:money

max_v = -1
max_items = None

'''
暴力解法
每个item共有2种状态：选、不选；
考察这些item所有可能状态的组合，计算每种组合的weight和value，并从中选取符合条件的最优解。
'''
for i in range(64):
    selector = {}
    for j in range(6):
        if ((i>>j) & 0x01) == 1:
            selector[j] = 1
        else:
            selector[j] = 0
    print('{}:{}'.format(i,selector))
    cw = 0
    cv = 0
    for k,v in selector.items():
        if v == 1:
            cw += item_w[k]
            cv += item_m[k]
    if cw <= b_weight and cv > max_v:
        max_v = cv
        max_items = {k:v for k,v in selector.items()}


print('max_v:{}'.format(max_v))
print('max_items:{}'.format(max_items))

'''
上述的暴力解法，效率较低。
原因在于：
  1、所有item的可能状态的组合比较多，计算量大；
  2、有些计算是重复的，比如相同value的情况，对于不同的weight组合计算了多次；
  3、有些计算是多余的，比如weight超过了约束条件，value其实没必要计算；
其实在计算中，存在着相同的状态，这个状态就是：{重量，当前重量的最大价值}
'''