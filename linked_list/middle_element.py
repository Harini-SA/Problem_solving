class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
n1 = Node(1)
n2 = Node(3)
n3 = Node(6)
n4 = Node(8)
n1.next = n2
n2.next =n3
n3.next = n4 

def insertInMiddle(head, x):
        #code here
        fast = head
        slow = head
        newNode = Node(x)

        if head is None:
            return newNode
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        newNode.next = slow.next
        slow.next = newNode
        current = head
        while current:
            print(current.data, end =" ")
            current = current.next
insertInMiddle(n1,30)            
