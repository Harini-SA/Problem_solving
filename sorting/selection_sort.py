def selectionSort(arr):
    for i in range(0, len(arr)-1):
        mini = i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
    return arr
arr = [4, 1, 3, 9, 7]
print(selectionSort(arr))