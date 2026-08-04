def nthUglyNumber(n: int) -> int:
        arr = [1]
        n2, n3,n5 = 0,0,0
        for i in range(n):
            next_num = min(arr[n2]*2, arr[n3]*3, arr[n5]*5)
            arr.append(next_num)
            if next_num == arr[n2]*2:
                n2 += 1
            if next_num == arr[n3]*3:
                n3 += 1
            if next_num == arr[n5]*5:
                n5 += 1
        return arr[n-1]
print(nthUglyNumber(n=10))