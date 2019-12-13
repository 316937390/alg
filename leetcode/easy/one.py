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
                
            
if __name__ == "__main__":
    print(find_two_nums_eq_target([1,5,2,7],0))
    print(find_two_nums_eq_target([3,-5,2,10],5))
