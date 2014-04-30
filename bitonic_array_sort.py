inc=[ i for i in range(10,250000)]
dec=[ i for i in range(0,50000)]
dec.reverse()
array=inc+dec
print max(array)
#print array

#array=[7,8,12,13,14,15,16,7,4,3,2,1]
def findMax(array,start,end,count):
   
   
   mid=(start+end)/2
   #print mid
   #print start,end
   
   count=count+1
   
   if array[mid]<array[mid-1]:
       findMax(array,start,mid-1,count)
   elif array[mid]<array[mid+1]:
       findMax(array,mid+1,end,count)
   else:
       print array[mid],mid,count
       return 
       """"
   while(start<mid<end):
       count+=1
       if array[mid]<array[mid-1]:
           mid=mid-1
       elif array[mid]<array[mid+1]:
           mid=mid+1
       else:
           return mid,count 
    """
    
    
findMax(array,0,len(array)-1,0)
