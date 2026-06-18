def largest(num):
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    if len(num) <3:
        return -1 
    for i in num:
        if i > first:
            third = second
            second = first
            first = i
        elif i> second :
            third = second
            second = i
        elif i > third:
            third = i
    return third 
nums = [2, 4, 1, 3, 5]
print(largest(nums))       
