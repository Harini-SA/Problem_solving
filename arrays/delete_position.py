from array import *
pos =2
arr = array('i',[1,2,2,4,5])
k = pos-1
for i in range(pos,len(arr)):
        arr[k]=arr[i] 
        k= k+1     
for i in range(0,k):
    print(arr[i])