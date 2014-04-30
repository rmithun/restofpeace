import random
import timeit

lists=[random.randint(0,3454554) for i in range(0,200000)]

start1=timeit.default_timer()
lists.sort()
end1=timeit.default_timer()

print lists[0]

print end1-start1


def mergeSort(lists):
    
    result=[]
    
    if len(lists)<2:
        return sorted(lists)
    mid=int(len(lists)/2)
    #print lists
    firsthalf=mergeSort(lists[0:mid])
    
    secondhalf=mergeSort(lists[mid:len(lists)])
    #print firsthalf,secondhalf
    i=0
    j=0
    while i < len(firsthalf) and j < len(secondhalf):
        if firsthalf[i]<secondhalf[j]:
            result.append(firsthalf[i])
            i+=1
        else:
            result.append(secondhalf[j])
            j+=1
    result+=firsthalf[i:]
    result+=secondhalf[j:]
    return result
start2=timeit.default_timer()
mergeSort(lists)
end2=timeit.default_timer()
print end2-start2
