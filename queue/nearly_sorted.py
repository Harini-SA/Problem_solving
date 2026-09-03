from collections import deque
def nearlySorted(arr, k):  
    n = len(arr)
    q = deque(arr[:k+1])
    i = k + 1
    index = 0

    while q:
        min_val = min(q)     
        q.remove(min_val) 
        arr[index] = min_val  
        index += 1
        if i < n:
            q.append(arr[i])
            i += 1
    return arr        
print(nearlySorted(arr= [2, 3, 1, 4], k = 2))            
            
        