from collections import deque
def reverseFirstK(q, k):
    if not q or k > len(q):
        return q
    if k <= 0:
        return q
    store = []
    for i in range(k):
        store.append(q.popleft())
    while store:
        q.append(store.pop())
    for i in range(len(q)-k):
        q.append(q.popleft())
    return q    
print(reverseFirstK(deque([1, 2, 3, 4, 5]), k = 3))
        