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
def delete(head,pos):
    curr = head
    for i in range(pos):
        if curr is None:
            break
        curr = curr.next
    if curr is None:
        return head
    if curr.next:
        curr.next.prev = curr.prev
    if curr.prev:    
        curr.prev.next = curr.next  
    return head        
       
    return head           
def print_dll(head):
    curr = head
    while curr:
        print(curr.data, end =" ")
        if curr.next is not None:
            print("<->", end =" ")
        curr = curr.next                
print_dll(delete(n1,1))  