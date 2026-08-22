def nextLargerElement(arr):
    n = len(arr)
    res = [-1]*n
    stack = []
    
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = arr[stack[-1]]
        stack.append(i)
    return res
print(nextLargerElement([1, 3, 2, 4]))