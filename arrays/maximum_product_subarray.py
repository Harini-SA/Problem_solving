nums = [-1, -3, -10, 0, 6]
def product_subarray(nums):
    prefix = 1
    suffix = 1
    max_arr = float('-inf')
    for i in range(len(nums)):
        prefix *= nums[i]
        suffix *= nums[len(nums)-1 -i]
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        max_arr = max(max_arr, max(prefix,suffix))
    return max_arr
print(product_subarray(nums))            
