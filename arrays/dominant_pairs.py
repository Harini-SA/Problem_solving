from array import *
arr = array('i',[10, 2, 2, 1])
n = len(arr)//2
first = (arr[ :n])
second = sorted(arr[n:])
right = 0 
count = 0
for left in range(n):
    while right <len(second) and first[left]>= 5*second[right]:
        right = (right+ 1)
        count = count +1
print(count)