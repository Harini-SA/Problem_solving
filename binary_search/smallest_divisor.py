import math
def smallestDivisor(nums,threshold):
        low = 1
        high = max(nums)
        while low<= high:
            mid = (low+high)//2
            if sumOfNum(mid,nums) <= threshold:
                high = mid -1
            else:
                low = mid+1
        return low
def sumOfNum(mid,nums):
        sum = 0
        for i in nums:
            sum += math.ceil(i/mid)
        return sum  
print(smallestDivisor([1,2,5,9], threshold = 6))  
        