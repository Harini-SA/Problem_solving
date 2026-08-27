def celebrity(mat):
    if len(mat) <2:
        return 0
    n = len(mat)
    st =[]
    for i in range(n):
        st.append(i)
    while len(st)>1:
        a = st.pop()
        b = st.pop()
        if mat[a][b] == 1:
            st.append(b)
        else:
            st.append(a)
    c = st.pop()
    
    for i in range(n):
        if i != c and (mat[c][i] == 1 or mat[i][c] == 0):
            return -1
    return c 
print(celebrity(mat= [[1, 1, 0],
                [0, 1, 0],
                [0, 1, 1]]))