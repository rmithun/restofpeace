s=[1,2,3,4,5,6,7]
def rev(ll,a,b):
    while a<b:
        temp=ll[a]
        ll[a]=ll[b]
        ll[b]=temp
        a=a+1
        b=b-1
    return ll     
d=2
n=len(s)
print rev(s,0,d-1)
print rev(s,d,n-1)
print rev(s,0,n-1)

