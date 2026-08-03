def smallestDistancePair(nums, k):
        nums.sort()
        high = nums[len(nums) -1] - nums[0]
        low = float('inf')
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] < low:
                low = nums[i] - nums[i-1]
        while low<=high:
            mid = (low+high) // 2
            if sliding(mid, nums) < k :
                low = mid+1
            else:
                high = mid -1
        return low        
def sliding(mid, nums):
        j = 0
        count = 0
        for i in range(1,len(nums)):
            while (nums[i] - nums[j]) > mid:
                j += 1
            count += i-j
        return count 
print(smallestDistancePair([1,6,1], k=3))       
                            
        