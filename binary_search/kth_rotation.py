value = [5, 1, 2, 3, 4]
def kth_rotation(value):
    low = 0
    high = len(value) -1
    ans = float('inf')
    index = -1
    while low <= high:
        mid = (low+high)//2
        if value[low] <= value[mid]:
            if ans> value[low]:
                ans = value[low]
                index = low
            low = mid+1
        else:
            if ans>value[high]:
                ans = value[high]
                index = high
            high = mid-1    
    return index
print(kth_rotation(value))                    