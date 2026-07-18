
def first_element(arr, x):
    low = 0
    high = len(arr)-1
    first =-1
    while low<=high:
        mid   =(  low+high )// 2
        if arr[mid] == x:
            first = mid
            high = mid -1
        elif arr[mid]<x:
            low =mid+1
        else:
             high = mid-1
    return first
def last_element(arr, x):
    low = 0
    high = len(arr)-1
    last = -1
    while low<=high:
        mid   =(  low+high )// 2
        if arr[mid] == x:
            last = mid
            low = mid +1
        elif arr[mid]<x:
            low =mid+1
        else:
            high = mid-1
    return last
        
                    
def find(arr, x):
    a = first_element(arr, x)
    b = last_element(arr, x)
    return [a, b]
        # code here
arr = [1,2,2,2,3,4,5]
x = 2
print(find(arr,x))