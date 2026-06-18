def three_sum(nums, target):
    nums.sort()
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j<k:
            total = nums[i]+nums[j]+nums[k]
            if total == target:
                return True
            elif total < target:
                j += 1
            elif total > target:
                k-=1
    return False
nums = [1, 4, 45, 6, 10, 8] 
target = 13
print(three_sum(nums,target))           
