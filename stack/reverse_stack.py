def reverseStack(st):
    temp = []
    while st:
        temp.append(st.pop())
    for i in temp:
        st.append(i)
    return st 
print(reverseStack([3, 2, 1]))   