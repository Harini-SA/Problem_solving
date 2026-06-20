nums = [1, 2, 8, 10, 10, 12, 19]
def floor(nums,k):
    low = 0
    high = len(nums)-1
    ans =  -1
    while low <= high:
       mid = (low+high) // 2
       if nums[mid] <= k:
           ans = mid
           low = mid+1
       else:
           high = mid -1
    return ans
print(floor(nums,k=5))           