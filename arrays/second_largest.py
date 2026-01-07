from array import *
arr = array('i',[5, 1, 9, 7, 9, 7])
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num>second and num!=first:
        second = num
else:
    if second ==  float('-inf'):
        print("no second largest")
print(second)