def removeLoop(head):
        if head is None or head.next is None:
            return 
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                if slow == head:
                    while fast.next != head:
                        fast = fast.next
                else:    
                    slow = head
                    while slow.next != fast.next:
                        slow = slow.next
                        fast = fast.next
                    
                fast.next = None
                break
            