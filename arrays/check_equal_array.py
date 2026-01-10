from array import *
from collections import Counter
arr = array('i',[1,2,3])
arr1 = array('i',[3,2,1])
if len(arr)!=len(arr1):
    print("not same")
else:
   freq = Counter(arr)
   for i in arr1:
       if i not in freq:
           print("not equal")
   else:
       print("same")
               
