def getfineElement(value,target,i,j,list_):
    print value,target
    if value==target:
        print "Element found"
        return 1
    elif value>target:
        getfineElement(list_[i-1][j],target,i-1,j,list_)
    elif value<target:
        getfineElement(list_[i][j+1],target,i,j-1,list_)
    else:
        return 0
    

list_=[[i*c+1 for c in range(2,5)]for i in range(1,4)]
min=list_[0][0]
max=list_[2][2]
target=10
import sys
if not min<target<max:
    print "Number not in MX"
    sys.exit(0)


if (getfineElement(list_[2][0],target,2,0,list_)):
    print "Found"
    
list2=[[i*c+1 for c in range(2,9)]for i in range(1,19)]
print "Rec search"
getfineEleRec(49,list2,0,len(list2))
