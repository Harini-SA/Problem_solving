def splitArray(arr, k):
        if k>len(arr):
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid =(low+high)//2
            maximum = maximumarr(arr,mid)
            if (maximum > k):
                low = mid+1
            else:
                high = mid -1
        return low
def maximumarr(arr,mid):
        maximum = 1 
        largestsum = 0
        for i in range(len(arr)):
            if (largestsum +arr[i]) <= mid:
                largestsum += arr[i]
            else:
                maximum += 1
                largestsum = arr[i]
        return maximum
print(splitArray([1, 2, 3, 4], k = 3))