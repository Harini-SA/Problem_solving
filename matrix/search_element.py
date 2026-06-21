def search_matrix(nums,target):
    low = 0
    m = len(nums)
    n = len(nums[0])
    high = (m*n)-1
    while low<=high:
        mid = (low+high)//2
        rows = mid // n
        cols = mid %n
        if nums[rows][cols] == target:
            return True
        elif nums[rows][cols]<target:
            low += 1
        else:
            high -= 1
    return False
nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search_matrix(nums,target))            
