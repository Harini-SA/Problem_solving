class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
n1 = Node(1)
n2 = Node(3)
n3 = Node(6)
n1.next = n2
n2.next =n3        


def reverseList( head):
        
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        while prev:
            print(prev.data, end = " ")
            if prev.next is not None:
                print("->", end =" ")
            prev = prev.next
reverseList(n1)            