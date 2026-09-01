from collections import deque, defaultdict
def firstNonRepeating(s):
    freq = defaultdict(int)
    q = deque()
    res = ""
    for i in s:
        q.append(i)
        freq[i] += 1
        while q and freq[q[0]] >1:
            q.popleft()
        if q:
            res += (q[0])
        else:
            res+="#"
    return res
print(firstNonRepeating("aabc"))	        
		