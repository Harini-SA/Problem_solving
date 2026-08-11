def pairwiseSwap(self, head):
    dummy = Node(0)
    first = head
    prev = dummy
    while first and first.next:
        second = first.next
        nextnode = first.next.next
        second.next = first
        first.next = nextnode
        prev.next = second
        prev = first
        first = nextnode
    return dummy.next