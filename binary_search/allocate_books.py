def findPages(arr, k):
        if k>len(arr):
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid =(low+high)//2
            student = maximumPage(arr,mid)
            if (student > k):
                low = mid+1
            else:
                high = mid -1
        return low
def maximumPage(arr,pages):
        student = 1 
        pagesstudent = 0
        for i in range(len(arr)):
            if (pagesstudent +arr[i]) <= pages:
                pagesstudent += arr[i]
            else:
                student += 1
                pagesstudent = arr[i]
        return student
print(findPages([12, 34, 67, 90],k=2))