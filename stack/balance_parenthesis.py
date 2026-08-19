def isBalanced(s):
    stack =[]
    top =-1
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack.append(s[i])
            top += 1
        else:
            if len(stack) == 0:
                return False
            if ((s[i] == ")" and stack[top] == "(") or (s[i] == "}" and stack[top] == "{") or
            (s[i] == "]" and stack[top] == "[")):
                stack.pop()
                top -= 1
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
print(isBalanced("{[()]}"))    