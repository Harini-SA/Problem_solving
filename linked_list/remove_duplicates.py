class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(5)
n2 = Node(5)
n3 = Node(7)
n4 = Node(6)
n5 = Node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
 
def removeDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
def print_ll(head):
    curr = head
    while curr:
        print(curr.data, end = " ")
        if curr.next is not None:
            print("->", end = " ")
        curr = curr.next    

removeDuplicates(n1)
print_ll(n1)