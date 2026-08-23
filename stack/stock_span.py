def calculateSpan(arr):
    n = len(arr)
    res = [-1] *n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if not stack:
            res[i] = i+1
        else:
            res[i] = (i-stack[-1]) 
        stack.append(i)
    return res
print(calculateSpan([100, 80, 90, 120]))