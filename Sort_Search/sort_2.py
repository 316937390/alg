# -*- coding: utf-8 -*-
from __future__ import print_function
from ADT.Stack import LStack

"""
归并排序：使用分治思想，先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并在一起，这样整个数组就都有序了。
分治是一种解决问题的处理思想，递归是一种编程技巧。
归并排序的时间复杂度分析：递归代码的时间复杂度也可以写成递推公式，如下：
                     T(n) = 2T(n/2)+n
归并排序的空间复杂度分析：在合并两个有序数组时，需要借助额外的存储空间，空间复杂度是O(n)
归并排序是稳定的，关键看merge()函数...
快速排序：如果要排序数组下标从p到r的数据，选择p到r之间的任意一个数据作为pivot(分区点)，遍历p到r之间的数据，将小于pivot的放到左边，将大于pivot的放到右边，将pivot放到中间，这样数组p到r之间的数据就被分成了三个部分，即[p,q-1], q, [q+1,r]，根据分治思想，可以递归地排序p到q-1之间的数据和q+1到r之间的数据，直到区间缩小为1，说明所有数据都有序了。
快速排序是不稳定的，因为分区的过程涉及交换操作...
快速排序的时间复杂度分析：最好情况（分区极其均衡）O(nlogn)，最坏情况（分区极其不均衡）O(n^2)，平均情况O(nlogn)
快速排序的空间复杂度分析：原地排序

如何优化快速排序：最坏情况下快速排序的时间复杂度是O(n^2)，主要原因是分区点选的不够合理，最理想的分区点是被分区点分开的两个分区中，数据的数量差不多。
三数取中法；随机法；
"""

##
def merge(arr, p, q, r):
    i = p
    j = q+1
    tmp = list()
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1
    for k in range(p,r+1,1):
        arr[k] = tmp[k-p]
##
def merge_sort_c(arr, p, r):
    if p >= r:
        return
    q = p + ((r-p)>>1)
    merge_sort_c(arr,p,q)
    merge_sort_c(arr,q+1,r)
    merge(arr,p,q,r)
##
def merge_sort(arr, n):
    merge_sort_c(arr,0,n-1)



##
def quick_sort(arr,n):
    quick_sort_c(arr,0,n-1)

def quick_sort_c(arr,p,r):
    if p >= r:
        return
    q = partition(arr,p,r)
    quick_sort_c(arr,p,q-1)
    quick_sort_c(arr,p+1,r)

def partition(arr,p,r):
    pivot = arr[r]
    i = p
    for j in range(p,r,1):
        if arr[j] < pivot:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
    tmp = arr[i]
    arr[i] = pivot
    arr[r] = tmp
    return i

##快速排序的非递归实现
def qsort(arr,n):
    if n == 1:
        return
    stack = LStack()
    p = 0
    r = n-1
    stack.push(r)
    stack.push(p)
    while stack.top() != None:
        p = stack.pop().data
        r = stack.pop().data
        q = partition(arr,p,r)
        if p >= (q-1) and (q+1) < r:
            stack.push(r)
            stack.push(q+1)
        if (q+1) >= r and p < (q-1):
            stack.push(q-1)
            stack.push(p)
        if p < (q-1) and (q+1) < r:
            stack.push(r)
            stack.push(q+1)
            stack.push(q-1)
            stack.push(p)

##求无序数组中的第K大元素，要求时间复杂度是O(n)
def k_th_arr(arr,k,n):
    return k_th_arr_c(arr,k,0,n-1)

def k_th_arr_c(arr,k,p,r):
    q = partition(arr,p,r)
    if k == (q+1):
        return arr[q]
    elif k < (q+1):
        return k_th_arr_c(arr,k,p,q-1)
    elif k > (q+1):
        return k_th_arr_c(arr,k,q+1,r)


if __name__ == "__main__":
    ##测试归并排序
    arr_1 = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    merge_sort(arr_1, len(arr_1))
    print(arr_1)
    ##测试快速排序
    arr_2 = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    quick_sort(arr_2, len(arr_2))
    print(arr_2)
    ##测试qsort
    arr_3 = [10,2,6,33,82,25,59,94,65,23,45,27,73,25,39,10]
    qsort(arr_3,len(arr_3))
    print(arr_3)
    ##
    k = 10
    arr_4 = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    th = k_th_arr(arr_4,k,len(arr_4))
    print("%dth : %d" % (k,th))
