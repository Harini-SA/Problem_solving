from array import *
arr = array('i',[1,2,3,4,6])
target = 6
left =0
right =len(arr)-1
while left <right:
    if arr[left] +arr[right]== target:
        print(arr[left],arr[right])
        break
    elif arr[left]+arr[right]<target:
        left += 1
    elif arr[left]+arr[right]>target:
        right -= 1
    else:
        print("no such numbers")