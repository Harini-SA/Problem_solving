from collections import deque
def minCost(arr):
    arr.sort()
    q1 = deque(arr)
    q2 = deque()
    total = 0
    
    def get_min():
        if q2 and (not q1 or q2[0] <= q1[0]):
            return q2.popleft()
        return q1.popleft()
        
    while len(q1) + len(q2) >1:
        a = get_min()
        b = get_min()
        cost = a + b
        total += cost
        q2.append(cost)
    return total
print(minCost([4, 3, 2, 6]))
        