class Node:
    def __init__(self,data):
        self.data = data
        self.next = None        
        self.prev = None
n1 = Node(1)
n2 = Node(3)
n2.prev = n1
n1.next = n2
n3 = Node(2)
n2.next = n3
n3.prev= n2
def insert(data,head):
    newnode = Node(data)
    newnode.next = head
    if head is not None:
        head.prev = newnode
    return newnode    
def print_dll(head):
    curr = head
    while curr:
        print(curr.data, end =" ")
        if curr.next is not None:
            print("<->", end =" ")
        curr = curr.next                       
print_dll(insert(5,n1) )                