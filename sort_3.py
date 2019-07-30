# -*- coding: utf-8 -*-
from __future__ import print_function


"""
线性排序：桶排序、计数排序、基数排序，时间复杂度O(n)
桶排序：将要排序的数据分到几个有序的桶里，每个桶里的数据再单独进行排序；桶内数据排完序后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了。

桶排序对数据的要求是很严苛的：首先，要排序的数据需要很容易就能划分成m个桶，且桶之间有着天然的大小顺序；其次，数据在各个桶之间的分布是比较均匀的。
桶排序适合用在外部排序中，即数据存储在外部磁盘上，数据量比较大，内存有限，无法将数据全部加载到内存中。

计数排序：当要排序的n个数据，所处的范围并不大的时候，比如最大值是k，就可以把数据划分成k个桶，每个桶内的数据的值都是相同的，省去了桶内排序的时间。
计数排序适用于数据范围不大的场景，而且只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。

基数排序：要排序的数据可以分割出独立的“位”来比较，而且位之间有递进的关系，除此之外，每一位的数据范围不能太大，要可以用线性排序算法来排序。注意：从低位到高位，按照每位来排序的算法必须是稳定的。
"""

##
def countingSort(arr, n):
    if n <= 1:
        return
    ##查找数据范围，假设都是非负整数
    max_v = arr[0]
    for i in range(n):
        if arr[i] > max_v:
            max_v = arr[i]
    ##申请一个计数数组
    cnt = [0]*(max_v+1)
    for i in range(n):
        cnt[arr[i]] += 1
    ##依次累加
    for i in range(1,len(cnt)):
        cnt[i] = cnt[i-1] + cnt[i]
    ##临时数组，存储排序后的结果
    tmp = [None]*n
    ##计数排序的关键步骤
    for i in range(n):
        index = cnt[arr[n-1-i]] - 1
        tmp[index] = arr[n-1-i]
        cnt[arr[n-1-i]] -= 1
    ##将结果拷贝
    for i in range(n):
        arr[i] = tmp[i]

##
def radixSort(arr,n,digit):
    if n <= 1:
        return
    for i in range(digit):
        radixSort_c(arr,n,digit-1-i)


def radixSort_c(arr,n,radix):
    max_v = int(arr[0][radix])
    for i in range(n):
        if int(arr[i][radix]) > max_v:
            max_v = int(arr[i][radix])
    cnt = [0]*(max_v+1)
    for i in range(n):
        cnt[int(arr[i][radix])] += 1
    for i in range(1,len(cnt)):
        cnt[i] = cnt[i-1] + cnt[i]
    tmp = [None]*n
    for i in range(n):
        index = cnt[int(arr[n-1-i][radix])] - 1
        tmp[index] = arr[n-1-i]
        cnt[int(arr[n-1-i][radix])] -= 1
    for i in range(n):
        arr[i] = tmp[i]

if __name__ == "__main__":
    ##测试计数排序
    arr_1 = [2,5,3,0,2,3,0,3]
    countingSort(arr_1, len(arr_1))
    print(arr_1)
    ##测试基数排序，手机号码排序
    arr_2 = ["13601090646","13121045042","13671131521","13718301518"]
    radixSort(arr_2,len(arr_2),11)
    print(arr_2)
