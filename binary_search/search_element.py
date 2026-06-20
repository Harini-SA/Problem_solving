nums = [1, 2, 3, 4, 6]
def binary(nums,k):
    low = 0
    high = len(nums) -1 
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == k:
            return True
        elif nums[mid] < k:
            low = mid+1
        else:
            high = mid-1
    return False
print(binary(nums,k = 6))             