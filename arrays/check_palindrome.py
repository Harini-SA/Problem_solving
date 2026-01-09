from arrays import *
arr =array('i',[1,2,3,2,1])
left =0
right =len(arr)-1
while left < right:                        
    if arr[left]!=arr[right]:
        print("not palindrome")
        break
    left +=1
    right -=1