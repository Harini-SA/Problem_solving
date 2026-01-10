from array import *
from collections import Counter
arr = array('i',[1,2,3])
arr1 = array('i',[3,2,1])
if len(arr)!=len(arr1):
    print("not same")
else:
    freq = Counter(arr)
    freq1 = Counter(arr1)
    for key in freq.keys():
        if freq[key] != freq1[key]:
           print("not equal")
           break
    else:
       print("same")
               
