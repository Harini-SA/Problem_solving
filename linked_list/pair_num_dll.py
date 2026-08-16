def findTail(head):
        tail = head
        while tail.next is not None:
            tail = tail.next
        return tail    
def givenSumPairs(self, head, target):
    left = head
    right = findTail(head)
    ans = []
    while left.data < right.data:
        if left.data + right.data == target:
            ans.append([left.data,right.data])
            left = left.next
            right = right.prev
        elif left.data +right.data <target:
            left = left.next
        else:
            right = right.prev
    return ans 
givenSumPairs(head,target)