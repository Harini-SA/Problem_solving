from array import *
arr = array('i',[4,7,19,16])
k=3
maximum = max(arr)
tot = 0
for i in range(len(arr)):
    difference = maximum - arr[i]
    if difference % k != 0:
        print("not possible to increment")
    else:
        tot = tot + difference // k
print(tot)