def findKthNumber(m, n, k):
        low = 1
        high = m*n
        while (low<= high):
            mid = (low+high) // 2
            if lessthan(mid, m, n) < k:
                 low = mid+1
            else:
                high = mid - 1
        return low
def lessthan(mid, m, n):
        total = 0
        for i in range(1,m+1):
            total += min(mid//i, n)
        return total 
print(findKthNumber(m = 3, n = 3, k = 5))   

        