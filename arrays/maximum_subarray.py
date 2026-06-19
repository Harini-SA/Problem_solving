nums = [5,4,-1,7,8]
def maximum(nums):
    sum_arr = 0
    max_arr = float('-inf')
    for i in range(len(nums)):
        sum_arr += nums[i]
        if sum_arr > max_arr:
            max_arr = sum_arr
        if sum_arr < 0:
            sum_arr = 0
    return max_arr
print(maximum(nums))            
