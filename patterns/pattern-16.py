""" A
    B B
    C C C
    D D D D
    E E E E E"""
for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end =" ")
    print()