""" 4444444
    4333334
    4322234
    4321234
    4322234
    4333334
    4444444 """
max_value = 4  #(n//2)+1
for i in range(7):
    rows =""
    for j in range(7):
        dist = min(i,j,7-i-1,7-j-1)
        value = max_value-dist
        rows+= str(value)
    print(rows)    
