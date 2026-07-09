""" E
    D E 
    C D E
    B C D E
    A B C D E"""
for i in range(5,-1,-1):
    for j in range((4-i),-1,-1):
        print(chr(65+(4-j)), end =" ")
    print()    