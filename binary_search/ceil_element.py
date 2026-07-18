nums = [1, 2, 8, 10, 10, 12, 19]
def ceil(nums,k):
    low = 0
    high = len(nums)-1
    ans =  -1
    while low <= high:
       mid = (low+high) // 2
       if nums[mid] >= k:
           ans = mid
           high = mid -1
       else:
           low = mid+1
    return ans
print(ceil(nums,k=5))           