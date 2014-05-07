import math

def nextPalindrome(nos):
    #import pdb;pdb.set_trace();
    str_no=str(nos)
    length=len(str_no)
    middle=length/2
    mid_ele=str(nos)[(len(str(nos))-1)/2]
    left=str_no[:middle]
    rev_lef=left[::-1]
    if len(str_no)%2!=0:
        inc=pow(10,length/2)
        new_no=int(left+mid_ele+rev_lef)
    else:
        inc=int(1.1*pow(10,length/2))
        new_no=int(left+rev_lef)
    print new_no,inc,str_no[middle],mid_ele
    if new_no>nos:
        return new_no,nos
    elif mid_ele!='9':
        return new_no+inc,nos
    else:
       return nextPalindrome(roundup(new_no)),nos
    #print new_no,nos
    
def roundup(num):
    length=len(str(num))
    inc=pow(10,(length/2)+1)
    return ((num/inc)+1)*inc
print nextPalindrome(int(raw_input()))

