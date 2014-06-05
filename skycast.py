"""



"""


import sys
channels_range=[]
try:
    channels_range=map(int,raw_input().split())
    channels=[0] +range(channels_range[0],channels_range[1]+1)
    if 0<channels_range[0]<channels_range[1]<10000:
        pass
    else:
        print "Please enter valid channel "
        sys.exit() 
    blocked=map(int,raw_input().split())
    if blocked[0] > 40:
        print "You can block only 40 channels"
        sys.exit()
    total_blocked=blocked[0]
    blocked=blocked[1:]
    for i in blocked:
        if i<50:
            print "You can block only channels greater than 50"
            sys.exit()
        if channels_range[1]>i<channels_range[0]:
            print "Block channels must be within the range"
            sys.exit()
    if len(blocked)!=total_blocked:
        print "Please block %s channels as per the input"%(total_blocked)
        sys.exit()
    for i in blocked:
        channels.remove(i)
except:
    print "Exception"
    sys.exit()

views=map(int,raw_input().split())

for i in views:
    if i not in  channels:
        print " Enter only valid channels"
        sys.exit()
        


previous=-10000
next=None
current=None
count=len(str(views[0]))
index_diff=0
if len(views)>1:
    current=views[0]
    next=views[1]
else:
    print 'Count %s'%(len(views))
    sys.exit()
for i in range(1, len(views)+1):
    
    if next!= previous:
        nxt_pre_diff=abs(next-previous)+1
        curr_next_diff=abs(current-next)
        next_len=len(str(next))
        index_diff=abs(channels.index(next)-channels.index(current))
        if next!=current:
            if nxt_pre_diff < next_len:
                if  nxt_pre_diff <curr_next_diff:
                    if index_diff > nxt_pre_diff:
                        count+=nxt_pre_diff
                    else:
                        count+=index_diff
                else:
                    if index_diff > curr_next_diff:
                        count+=curr_next_diff
                    else:
                        count+=index_diff
            else:
                if next_len < curr_next_diff:
                    if index_diff > next_len:
                        count+=next_len
                    else:
                        count+=index_diff
    
                else:
                    if index_diff > curr_next_diff:
                        count+=curr_next_diff
                    else:
                        count+=index_diff
        else:
            count+=0

    else:
        count+=1
    
    previous=current
    current=next
    try:
        next=views[i+1]
    except:
        break
print "count  "+str(count)
    
        

        
    
