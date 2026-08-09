class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n7 =Node(7)
n1.next = n2
n2.next = n3
n4 = Node(5)
n5 = Node(6)
n4.next =n5
head1 = n1
head2 = n4 

def makeUnion(head1, head2):
    seen = {}
    result = []
    while head1:
        if head1.data not in seen:
            seen[head1.data] =1
            result.append(head1.data)
        head1 = head1.next
    while head2:
        if head2.data not in seen:
            seen[head2.data]=1
            result.append(head2.data)
        head2 = head2.next  
    head = Node(result[0])
    current = head
    for values in result[1:] :
        newnode = Node(values)
        current.next = newnode
        current = current.next
    while head:
        print(head.data, end =" ")
        if head.next is not None:
            print("->" , end =" ") 
        head = head.next       
makeUnion(head1, head2)
