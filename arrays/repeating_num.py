def repeat(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1
    for key, values in freq.items():
        if freq[key]>1:
            print(key, end=" ")    

repeat([1,4,2,3,4,2])