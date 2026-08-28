def countMinReversals(s):
    stack =[]
    if len(s)%2 == 1:
        return -1
    for i in s:
        if i == "}" and stack:
            if stack[-1] == "{":
                stack.pop()
            else:
                stack.append("}")
        else:
            stack.append(i)
    value= len(stack)
    n= 0
    while stack:
        if stack[-1] == "{":
            n += 1
        stack.pop()
    return value // 2 + n%2  
print(countMinReversals("}{{}}{{{"))