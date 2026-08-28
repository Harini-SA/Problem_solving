def reducedString(k, s):
    stack = []
    ans = ""
    if k == 1:
        return ""
    for char in s:
        if not stack:
            stack.append((char,1))
        else:
            if char == stack[-1][0]:
                p = stack.pop()
                if p[1]+1<k:
                    stack.append((p[0],p[1]+1))
            else:
                stack.append((char,1))
    while stack:
        if stack[-1][1]>1:
            count = stack[-1][1]
            ans += stack[-1][0] * count
        else:
            ans += stack[-1][0]
        stack.pop()
    return ans[::-1]
print(reducedString(2,"geeksforgeeks"))    
        