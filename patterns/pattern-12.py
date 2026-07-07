for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    for j in range((4-i)*2):
        print(" ", end ="")
    for j in range(i,0,-1):
        print(j, end="")
    print()  
