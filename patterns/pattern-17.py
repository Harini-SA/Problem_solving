"""       A       
        A B A
      A B C B A
    A B C D C B A
  A B C D E D C B A"""

for i in range(5):
    k =0
    print((5-i-1)*" ", end =" ")
    for j in range(1,(2*i)+2):
        print(chr(65+k), end ="")
        if j<=(((2*i)+1)//2)+1:
            k += 1
        else:
            k -= 1
    print()            
