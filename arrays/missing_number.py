from array import *
arr =array('i',[1,2,3,5,6,7])
n= len(arr)+1
total = (n*(n+1))//2
missing = total - sum(arr)
print("missing is:",missing)