class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(5)
n2 = Node(10)
n3 = Node(15) 
n1.next = n2
n2.next = n3 
def insert_at(position,data):
    current = n1
    for i in range(position-1):
        if current is None:
            raise IndexError("out of range")
        current = current.next
    newNode = Node(data)
    newNode.next = current.next
    current.next = newNode
    
insert_at(2,25)
current = n1
while current:
    print(current.data)
    current = current.next

        

             