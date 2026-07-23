def minDays(bloomDay, m, k) :
        if k *m > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = (low+high)//2
            if no_of_bouquets(bloomDay,m,k,mid):
                high = mid-1
            else:
                low = mid+1
        return low
def no_of_bouquets(bloomDay,m,k,days):
        count =0
        flowers = 0
        for i in range(len(bloomDay)):
            if bloomDay[i]<= days:
                count += 1
            else:
                flowers += count//k
                count = 0
        flowers += count //k
        if flowers >= m:
            return True
print(minDays([7,7,7,7,12,7,7],m =2, k =3))        