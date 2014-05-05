def findMaxsub(array):
    if len(array)==1:
        return array[0]
    elif len(array)==2:
        return max(array[0],array[1])
    secondlast=array[0]
    last=max(secondlast,array[1])
    current=last
    print current,secondlast,last
    for i in range(2,len(array)):
        current=max(array[i],max(secondlast+array[i],last))
        secondlast=last
        last=current
        print current,secondlast,last,array[i]
    return current


array=[3,2,5,10,7]
print findMaxsub(array)
