# -*- coding: utf-8 -*-
from __future__ import print_function


"""
如何分析一个“排序算法”
排序算法的执行效率：最好情况、最坏情况、平均情况时间复杂度；时间复杂度的系数、常数、低阶；比较次数和交换（或移动）次数
排序算法的内存消耗：空间复杂度，原地排序
排序算法的稳定性：稳定性是指如果待排序的序列中存在值相等的元素，经过排序之后，相等元素之间原有的先后顺序不变
有序度：数组中具有有序关系的元素对的个数
有序元素对：a[i] <= a[j], 如果 i < j。
逆序元素对：a[i] > a[j], 如果 i < j。
满有序度：完全有序数组的有序度，n*(n-1)/2
逆序度 = 满有序度 - 有序度
排序的过程就是增加有序度，减少逆序度，最后达到满有序度。

1.冒泡排序：冒泡排序只会操作相邻的两个数据，一次冒泡会让至少一个元素移动到它应该在的位置，重复n次，就完成了n个数据的排序工作。
2.插入排序：取未排序区间中的元素，在已排序区间中找到合适的位置将其插入，并保证已排序区间数据一直有序，重复这个过程，直到未排序区间中元素为空，排序结束。
3.选择排序：每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。

冒泡排序 vs 插入排序：两者虽然在时间复杂度上一样，但是如果希望性能优化，则首选插入排序，插入排序也可以继续优化，比如：希尔排序

希尔排序：也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是不稳定的，最重要的是步长的选择，只要最终步长为1任何步长序列都可以工作。
"""

##
def bubble_sort(array_input):
    for i in range(len(array_input)):
        swap_flag  = False
        for j in range(len(array_input)-i-1):
            if array_input[j] > array_input[j+1]:
                tmp = array_input[j+1]
                array_input[j+1] = array_input[j]
                array_input[j] = tmp
                swap_flag = True
        if not swap_flag:
            break


##
def insert_sort(array_input):
    for i in range(1,len(array_input),1):
        value = array_input[i]
        j = i - 1
        while j >= 0:
            if value < array_input[j]:
                array_input[j+1] = array_input[j]
                j -= 1
            else:
                break
        array_input[j+1] = value

##
def select_sort(array_input):
    for i in range(len(array_input)):
        min_v = array_input[i]
        idx = i
        flag = False
        for j in range(i,len(array_input),1):
            if array_input[j] < min_v:
                min_v = array_input[j]
                idx = j
                flag = True
        if flag:
            tmp = array_input[i]
            array_input[i] = array_input[idx]
            array_input[idx] = tmp


##
def shell_sort(array_input):
    n = len(array_input)
    gap = (n >> 1)
    while gap > 0:
        for i in range(gap,n):
            value = array_input[i]
            j = i
            while j >= gap and value < array_input[j-gap]:
                array_input[j] = array_input[j-gap]
                j -= gap
            array_input[j] = value
        gap = (gap >> 1)



if __name__ == "__main__":
    ##测试冒泡排序
    arr_1 = [4,5,3,1,8,8,2]
    bubble_sort(arr_1)
    print(arr_1)
    ##测试插入排序
    arr_2 = [1,1,7,2,8,6,5,4,2]
    insert_sort(arr_2)
    print(arr_2)
    ##测试选择排序
    arr_3 = [5,8,5,3,2,7,6]
    select_sort(arr_3)
    print(arr_3)
    ##测试希尔排序
    arr_4 = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    shell_sort(arr_4)
    print(arr_4)
