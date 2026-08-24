def insertAtBottom(st,x):
        temp = []
        while st:
            temp.append(st.pop())
        st.append(x)
        while temp:
            st.append(temp.pop())
        return st
print(insertAtBottom([4, 3, 2, 1, 8],7))