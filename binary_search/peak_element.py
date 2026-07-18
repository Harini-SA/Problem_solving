nums = [1, 2, 4, 5, 7, 8, 3]
def peakElement(self, arr):
    
    if len(arr)==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[len(arr)-1]>arr[len(arr)-2]:
        return len(arr)-1
    low = 1
    high = len(arr)-2
    while low<= high:
        mid =(   low+high  )//2
        if arr[mid]> arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            low = mid+1
        else:
            high = mid-1