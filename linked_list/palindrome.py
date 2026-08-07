class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
n1 = Node(1)
n2 = Node(3)
n3 = Node(1)
n1.next = n2
n2.next =n3  


def isPalindrome(head):
        # code here
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev =None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True
print(isPalindrome(n1))