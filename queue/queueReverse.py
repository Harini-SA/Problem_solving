from collections import deque
def reverseQueue(q):
    st = []
    while q:
        st.append(q.popleft())
    while st:
        q.append(st.pop())
    return q 
print(reverseQueue(deque([5,10,15,20])))