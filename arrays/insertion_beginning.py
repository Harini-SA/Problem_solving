from array import *
arr = array('i',[10,20,30,40])
n =4
arr.append(0)
element = 50
for i in range(n-1,-1,-1):
    arr[i+1] = arr[i]
arr[0]=element
print(arr)