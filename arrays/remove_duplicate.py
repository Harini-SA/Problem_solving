from array import *
arr = array('i',[1,2,2,3,4])
count =1
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
        arr[count]=arr[i]
        count +=1
for i in range(count):
    print(arr[i])        
        