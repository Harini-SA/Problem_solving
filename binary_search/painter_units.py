def maximumPartition(arr,partition):
        painter = 1 
        units = 0
        for i in range(len(arr)):
            if (units +arr[i]) <= partition:
                units+= arr[i]
            else:
                painter += 1
                units = arr[i]
        return painter 
def minTime (arr, k):
        if k>len(arr):
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid =(low+high)//2
            painter= maximumPartition(arr,mid)
            if (painter > k):
                low = mid+1
            else:
                high = mid -1
        return low
print(minTime([5, 10, 30, 20, 15],k=3))