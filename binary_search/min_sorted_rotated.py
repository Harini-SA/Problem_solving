def minimum(arr):
    low = 0
    high = len(arr)-1
    ans = float('inf')
    while low <= high:
        mid = (low+high) //2
        if arr[low] <= arr[mid]:
            ans = min(arr[low], ans)
            low = mid+1
        else:
            high = mid -1
            ans = min(ans, arr[mid])
    return ans  
arr = [5,6,7,1,2,3,4]   
print(minimum(arr))       