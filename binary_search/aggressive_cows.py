def aggressiveCows(arr, k):
        arr.sort()
        low = 1
        high = arr[len(arr)-1] - arr[0]
        while low <= high:
            mid = (low+high) // 2
            if canPlaceCows(arr,mid,k) == True:
                low = mid+1
                ans = mid
            else:
                high = mid-1
        return ans
def canPlaceCows(arr,mid,k):
        count = 1 
        last = arr[0]
        for i in range(1,len(arr)):
            if arr[i] -last >= mid:
                last = arr[i]
                count += 1
            if count>= k:
                return True
        else:
            return False
print(aggressiveCows([1, 2, 4, 8, 9],k=3))        