s=[1,0,1,0,1,1,1,1,0,1,1,0,1]
test=[0, 1, 0, 1, 0,1,0]


def findlargestsub0n1(y,x):
	
	#import pdb;pdb.set_trace()
	sum=0
	maxsize=-1
	fromindex=''
	for i in range(0,x):
		if y[i]==0:
			sum=-1
		else:
			sum=1
		for k  in range(i+1,x):
			if y[k]==0:
				sum+=-1
			else:		
				sum+=1

			if sum==0 and maxsize<k-i+1:
				maxsize=k-i+1
				fromindex=i
			

	return fromindex, maxsize+fromindex-1


print findlargestsub0n1(test,len(test))
