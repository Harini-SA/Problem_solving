from array import *

arr = list("flowers are beautiful")
left = 0
right = len(arr) - 1
while left < right:
    if arr[left] == " ":
        left += 1
    elif arr[right] == " ":
        right -= 1
    else:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
arr = "".join(arr)
print(arr)
