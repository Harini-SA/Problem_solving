def count(self,node):
        count = 1
        curr = node
        while curr.next != node:
            count +=1
            curr  = curr.next
        return count    
            
            
def lengthOfLoop(self, head):
    #code here
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return self.count(slow)
    return 0