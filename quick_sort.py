
import random
def qsort(lists):
    if lists==[]:
        return []
    else:
        pivot=lists[0]
        fh=qsort([x for x in lists[1:] if x<pivot])
        sh=qsort([x for x in lists[1:] if x>=pivot])
        return fh+[pivot]+sh


lists=[random.randint(0,100) for i in range(0,10)]

print qsort(lists)
