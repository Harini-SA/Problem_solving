class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n7 =Node(7)
n1.next = n2
n2.next = n3
n3.next = n7
n4 = Node(5)
n5 = Node(6)
n6  = n3
n8 = n7
n4.next =n5
n5.next = n6
n6.next = n8
head1 = n1
head2 = n4 



def intersectPoint(head1, head2):
        if head1 == None or head2 == None:
            return None
        temp1 = head1
        temp2 = head2
        while (temp1!= temp2):
            temp1 = temp1.next
            temp2 = temp2.next
            if temp1 == temp2:
                return temp1.data
            
            if temp1 == None:
                temp1  = head2
            if temp2 == None:
                temp2 =  head1
print(intersectPoint(head1, head2))                