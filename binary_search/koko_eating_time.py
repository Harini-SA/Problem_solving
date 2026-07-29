import math
def minEatingSpeed(arr, h):
        low =1 
        high = max(arr)
        while low <= high:
            mid =( low+high  )//2
            if totalhours(arr,mid) <= h:
                high = mid -1
            else:
                low = mid+1
        return low
def totalhours(arr, mid):
        totalh = 0
        for i in range(len(arr)):
            totalh += math.ceil(arr[i]/mid) 
        return totalh 
print(minEatingSpeed(arr=[3,6,7,11], h=8))   

        