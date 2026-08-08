class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
n1= Node(1)
n2= Node(2)
n3= Node(3)
n4= Node(4)
n1.next = n2
n2.next = n3
n3.next = n4

def deleteNode(x):
        x.data = x.next.data
        x.next= x.next.next
deleteNode(n3)
current = n1
while current:
    print(current.data, end = " ")
    if current.next is not None:
          print("->", end =" ")  
    current = current.next

         