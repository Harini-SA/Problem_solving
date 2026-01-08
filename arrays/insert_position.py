from array import *
arr = array('i',[10,20,30,40,0])
pos =3
element = 50
for i in range(4-1,pos -2,-1):
    arr[i+1] = arr[i]
arr[pos-1]=element     
print(arr)