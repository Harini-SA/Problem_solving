nums = [3,2,3]
def majority(nums):
    el =0
    count = 0
    for i in nums:
        if count == 0:
            el = i
            count += 1
        elif i != el:
            count -= 1 
        else:
            count += 1
    count1 = 0
    for i in nums:
        if i == el:
            count1 += 1
    if count1 > len(nums)/2:
        return el
print(majority(nums))    
