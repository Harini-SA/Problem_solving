def leastWeightCapacity(arr, D):
       low  = max(arr)
       high = sum(arr)
       while low <= high:
            mid = (low+high)//2
            if capacity(arr,mid) <= D:
                high = mid-1
            else: 
                low = mid+1
       return low
def capacity(arr,mid):
        days = 1   
        load = 0
        for i in range(len(arr)):
            if arr[i]+load > mid:
                days += 1
                load = arr[i]
            else:
                load += arr[i]
        return days  
print(leastWeightCapacity( arr=[1,2,3,4,5,6,7,8,9,10], D= 5))      
                