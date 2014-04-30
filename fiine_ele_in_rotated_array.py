###find an element in an sorted array which is rotated unkown time
import random
def findEle(array,key,start,end):
    mid=(start+end)/2
    print start,end,mid
    
    if array[mid]==key:
        return mid
    if end<start:
        return 0
    if array[mid] > array[start]:
        if key <= array[mid] and key >= array[start]:
            return findEle(array,key,start,mid-1)
        else:
            return findEle(array, key,mid+1, end)
    elif array[mid] < array[start]:
        if key >= array[mid] and key <= array[end]:
            return findEle(array,key,mid+1,end)
        else:
            return findEle(array, key, start, mid-1)
    elif array[start]==array[mid]:
        if array[mid]!=array[end]:
            return findEle(array, key, mid+1, end)
        else:
            result=findEle(array,key,start,mid-1)
            if result== -1:
                return findEle(array,key,mid+1,end)
            else:
                return result
    return -1

array=[10,15,20,0,5]
print array

print findEle(array,5,0,len(array))    
        
