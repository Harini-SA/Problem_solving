def priority(c):
            if c == "^":
                return 3
            elif c == "*" or c== "/":
                return 2
            elif c == "+" or c== "-":
                return 1
            else:
                return -1
        
def rightassociative(c):
    return c == "^"
def infixToPostfix(s):
    stack =[]
    res =[]
    
    for c in s:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            res.append(c)
        elif c== "(":
            stack.append("(")
        elif c == ")":
            while stack and stack[-1] != "(":
                res.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while stack and stack[-1] != "("  and (priority(c)<priority(stack[-1])or (priority(c) == priority(stack[-1]) and not rightassociative(c))):
                res.append(stack.pop())
            stack.append(c)
    while stack:
        res.append(stack.pop())
    return "".join(res)  
print(infixToPostfix("a*(b+c)/d"))