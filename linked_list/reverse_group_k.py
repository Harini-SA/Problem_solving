class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(5)
n5 = Node(6)
n7 =Node(7)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next =n5
n5.next = n7
head = n1

def reverseKGroup(head, k):
        # Code here
        if head is None:
            return head

        curr = head
        newHead = None
        tail = None
        while curr:
            prev = None
            new = None
            grouphead = curr
            count = 0
            while curr and count <k:
                new = curr.next
                curr.next = prev
                prev = curr
                curr = new
                count += 1
                
            if newHead is None:
                newHead  = prev
                    
            if tail is not None:
                tail.next = prev
            tail = grouphead
        return newHead 
def print_ll(head):
     current = head
     while current:
        print(current.data, end= " ")
        if current.next is not None:
           print("->" , end=" ")
        current = current.next
print_ll(reverseKGroup(head,4))        