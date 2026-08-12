class Node:
     def __init__(self,data):
          self.data = data
          self.next = None
n1 = Node(1)
n2 = Node(4)
n3 = Node(9)
n1.next = n2
n2.next = n3
def addOne(head):
        # code here
        carry = helper(head)
        if carry == 1:
            new = Node(carry)
            new.next = head
            return new
        return head  
def helper(temp):
        if temp == None:
            return 1
        carry = helper(temp.next)
        temp.data = temp.data + carry
        if temp.data < 10:
            return 0
        else:
            temp.data = 0
            return 1  
def print_ll(head):
     while head:
        print(head.data, end =" ")
        if head is not None:
            print("->", end = " ")
        head = head.next
print_ll(addOne(n1))          