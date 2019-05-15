# -*- coding: utf-8 -*-
lst = [4,5,6,1,2,3]


def find(a, low, high, value):
    while low <= high:
        mid  = low + (high-low)/2
        if a[mid] == value:
            return mid
        ##前半部分是有序的，后半部分是循环有序
        elif a[low] <= a[mid]:
            if a[mid] > value and a[low] <= value:
                high = mid - 1
            else:
                return find(a,mid+1, high,value)
        ##后半部分是有序的，前半部分是循环有序的
        elif a[low] > a[mid]:
            if a[mid] < value and a[high] >= value:
                low = mid + 1
            else:
                return find(a,low,mid-1,value)
    return -1

print(find(lst,0,len(lst)-1,4))
print(find(lst,0,len(lst)-1,5))
print(find(lst,0,len(lst)-1,6))
print(find(lst,0,len(lst)-1,1))
print(find(lst,0,len(lst)-1,2))
print(find(lst,0,len(lst)-1,3))
print(find(lst,0,len(lst)-1,7))
            
