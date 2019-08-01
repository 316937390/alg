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
