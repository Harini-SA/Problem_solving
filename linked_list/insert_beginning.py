class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1  = Node(5)
n2 = Node(10)
n3 = Node(15) 
n1.next = n2
n2.next = n3       
def insert_at(data):
    newNode = Node(data)
    newNode.next = n1 
    return newNode
current = insert_at(1,)
while current:
    print(current.data)
    current = current.next


