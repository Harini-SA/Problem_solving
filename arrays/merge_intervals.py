arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
def merge(arr):
    if not arr:
        return []
    arr.sort()
    res = []
    res.append(arr[0])
    for i in range(1, len(arr)):
        current = arr[i]
        last = res[-1]
        if current[0] <= last[1]:
            last[1] = max(current[1], last[1])
        else:
            res.append(current)
    return res

print(merge(arr))