from array import *
arr =array('i',[10,20,30,40])
for i in range(1,len(arr)):
    arr[i-1]=arr[i]
for i in range(len(arr)-1):
    print(arr[i])