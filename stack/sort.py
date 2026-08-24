def sortinsert(st, x):
    if not st or st[-1] <= x:
        st.append(x)
        return
    top = st.pop()
    sortinsert(st, x)
    st.append(top)
    
def sortStack(st): 
    if not st:
        return
    top = st.pop()
    sortStack(st)
    sortinsert(st, top)
def print_st(st):    
    sortStack(st=[41, 3, 32, 2, 11]) 
    print(st)
print_st([41, 3, 32, 2, 11])    
  