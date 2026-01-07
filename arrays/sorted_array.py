from array import *
arr = array('i',[4,3,6,1])
i=0
while i <len(arr)-1:
    if arr[i]<arr[i+1]:
       pass
    else:
        print("not sorted")
        break
    i=i+1
else:
    print("sorted")