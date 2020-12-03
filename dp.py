# -*- coding: utf-8 -*-

b_weight = 20 #背包重量
item_w = {0:3,1:5,2:10,3:8,4:1,5:6} # key:物品 value:weight
item_m = {0:6,1:20,2:5,3:7,4:3,5:4} # key:物品 value:money

max_v = -1
max_items = None

'''
暴力解法
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