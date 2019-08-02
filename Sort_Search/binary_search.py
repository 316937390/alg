# -*- coding: utf-8 -*-
from __future__ import print_function

"""
二分查找：针对有序的数据集合，每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为0。
二分查找的时间复杂度：O(logn)
二分查找的递归和非递归实现：1、循环退出条件   2、mid的取值    3、low和high的更新

二分查找应用场景的局限性：
1、二分查找依赖的是顺序表结构，即数组
2、二分查找针对的是有序数据：只能用在插入、删除操作不频繁，一次排序多次查找的场景中；针对动态变化的数据集合，二分查找将不再适用
3、数据量太小不适合二分查找：特例是如果数据之间的比较操作非常耗时，不管数据量大小，都推荐使用二分查找，因为可以有效减少比较次数
4、数据量太大也不适合二分查找

二分查找的变形问题：
1、查找第一个值等于给定值的元素
2、查找最后一个值等于给定值的元素
3、查找第一个大于等于给定值的元素
4、查找最后一个小于等于给定值的元素
"""

##非递归实现二分查找
def bsearch(arr, n, value):
    low = 0
    high = n-1
    while low<=high:
        mid = low + ((high-low)>>1)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid-1
        elif arr[mid] < value:
            low = mid+1
    return -1

##递归实现二分查找
def b_search(arr, low, high, value):
    if low > high:
        return -1
    mid = low + ((high-low)>>1)
    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return b_search(arr,low,mid-1,value)
    elif arr[mid] < value:
        return b_search(arr,mid+1,high,value)



##
def sqrt_b(v,precise):
    assert v>=0
    low = None
    high = None
    if v == 1:
        return 1
    if v == 0:
        return 0
    if v > 0  and  v < 1 :
        low = v
        high = 1
    elif v > 1 :
        low = 1
        high = v
    while low<=high:
        mid = low + ((high-low)/2)
        if (mid-precise)**2 < v and (mid+precise)**2 > v:
            return mid
        elif mid**2 > v:
            high = mid
        elif mid**2 < v:
            low = mid


##查找第一个值等于给定值的元素
def bs_first_eq(arr,n,value):
    low = 0
    high = n-1
    while low<=high:
        mid = low + ((high-low)>>1)
        if arr[mid] == value and (mid == 0 or arr[mid-1] < value):
            return mid
        elif arr[mid] == value and arr[mid-1] == value:
            high = mid-1
        elif arr[mid] < value:
            low = mid+1
        elif arr[mid] > value:
            high = mid-1
    return -1

##查找最后一个值等于给定值的元素
def bs_last_eq(arr,n,value):
    low = 0
    high = n-1
    while low<=high:
        mid = low + ((high-low)>>1)
        if arr[mid] == value and (mid == (n-1) or arr[mid+1] > value):
            return mid
        elif arr[mid] == value and arr[mid+1] == value:
            low = mid+1
        elif arr[mid] < value:
            low = mid+1
        elif arr[mid] > value:
            high = mid-1
    return -1

##查找第一个大于等于给定值的元素
def bs_first_ge(arr,n,value):
    low = 0
    high = n-1
    while low<=high:
        mid = low + ((high-low)>>1)
        if arr[mid] >= value and (mid == 0 or arr[mid-1] < value):
            return mid
        elif arr[mid] >= value and arr[mid-1] >= value:
            high = mid-1
        elif arr[mid] < value:
            low = mid+1
    return -1


##查找最后一个小于等于给定值的元素
def bs_last_le(arr,n,value):
    low = 0
    high = n-1
    while low<=high:
        mid = low + ((high-low)>>1)
        if arr[mid] <= value and (mid == (n-1) or arr[mid+1] > value):
            return mid
        elif arr[mid] <= value and arr[mid+1] <= value:
            low = mid+1
        elif arr[mid] > value:
            high = mid-1
    return -1




if __name__ == "__main__":
    ##测试非递归的二分查找
    arr_1 = [10]
    print(bsearch(arr_1,len(arr_1),9))
    arr_2 = [8,11,19,23,27,33,45,55,67,98]
    print(bsearch(arr_2,len(arr_2),55))
    ##测试递归的二分查找
    arr_3 = [5]
    print(b_search(arr_3,0,len(arr_3)-1,10))
    arr_4 = [8,11,19,23,27,33,45,55,67,98]
    print(b_search(arr_4,0,len(arr_4)-1,55))
    ##测试sqrt_b
    print("sqrt:",sqrt_b(5.0,0.0001))
    print("sqrt:",sqrt_b(1.0,0.0001))
    print("sqrt:",sqrt_b(0.0,0.0001))
    ##测试二分查找的变形问题
    arr_5 = [0,1,2,4,4,4,5,7,9,10]
    print("idx:",bs_first_eq(arr_5,len(arr_5),4))
    print("idx:",bs_first_eq(arr_5,len(arr_5),10))
    print("idx:",bs_first_eq(arr_5,len(arr_5),0))
    arr_7 = [0,0,0,1,2,4,4,4,5,7,9,10]
    print("idx:",bs_last_eq(arr_7,len(arr_7),0))
    print("idx:",bs_last_eq(arr_7,len(arr_7),4))
    print("idx:",bs_last_eq(arr_7,len(arr_7),10))
    arr_8 = [0,1,2,3,4,4,4,7,8,9]
    print("idx:",bs_first_ge(arr_8,len(arr_8),0))
    print("idx:",bs_first_ge(arr_8,len(arr_8),4))
    print("idx:",bs_first_ge(arr_8,len(arr_8),9))
    arr_9 = [0,1,2,3,4,4,5,7,8,9]
    print("idx:",bs_last_le(arr_9,len(arr_9),6))
    print("idx:",bs_last_le(arr_9,len(arr_9),0))
    print("idx:",bs_last_le(arr_9,len(arr_9),9))
