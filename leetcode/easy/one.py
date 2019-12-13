# -*- coding: utf-8 -*-
from __future__ import print_function

'''
1.两数之和
nums  target
'''
def find_two_nums_eq_target(nums=[], target=0):
    assert len(nums) > 0
    length = len(nums)
    result = {}
    for index, item in enumerate(nums):
        for i in range(index+1,length):
            if nums[i] + item == target :
                if result.get((index,i)) == None:
                    result[(index,i)] = True
    return [k for k,v in result.items()]


'''
整数反转
'''
def reverse_signed_int32(num):
    if num == 0 :
        return 0
    num_tmp = ""
    if num < 0 :
        num_tmp = str(-num)
    else:
        num_tmp = str(num)
    s_min = -(1<<31)
    s_max = (1<<31)-1
    sum = 0
    for index in range(len(num_tmp)) :
        sum += int(num_tmp[index])*(10**index)
    if num < 0 and sum > (s_max+1) :
        return 0
    if num > 0 and sum > s_max :
        return 0
    if num > 0 :
        return sum
    else:
        return -sum



if __name__ == "__main__":
    print(find_two_nums_eq_target([1,5,2,7],0))
    print(find_two_nums_eq_target([3,-5,2,10],5))
    print(reverse_signed_int32(-210))
    print(reverse_signed_int32(-2107))
    print(reverse_signed_int32((1<<31)-7))
    print(reverse_signed_int32(1<<31))
    print(reverse_signed_int32(-((1<<31)-7)))
    print(reverse_signed_int32(-(1<<31)))
