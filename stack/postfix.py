import math
def evaluatePostfix(arr):
    stack = []
    for token in arr:
        if token[0].isdigit() or (len(token)>1 and token[0]== "-"):
            stack.append(int(token))
        else:
            val1 = stack.pop()
            val2 = stack.pop()

            if token == '+':
                stack.append(val2 + val1)
            elif token == '-':
                stack.append(val2 - val1)
            elif token == '*':
                stack.append(val2 * val1)
            elif token == '/':
                stack.append(val2 // val1)
            elif token == '^':
                stack.append(int(math.pow(val2, val1)))
    return stack.pop()
print(evaluatePostfix(["2", "3", "1", "*", "+", "9", "-"]))
        