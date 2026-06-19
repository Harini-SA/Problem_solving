nums = [-5, 8, -14, 2, 4, 12]
k= -5
def longest_substring(nums,k):
    prefix_sum = 0
    sum_index ={}
    max_len = 0
    for i,num in enumerate(nums):
        prefix_sum += num
        if prefix_sum == k:
            max_len = i+1
        if (prefix_sum - k) in sum_index:
            max_len = max(max_len, i-sum_index[prefix_sum - k])
        if prefix_sum not in sum_index :
            sum_index[prefix_sum] = i
    return max_len
print(longest_substring(nums,k))
        
