class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(1)
n2 = Node(5)
n3 = Node(4)
n4 = Node(2)
n5 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def getmiddle(head):
        slow  = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
def merge(list1,list2):
    prev= Node(0)
    curr = prev
    while list1 != None and list2 != None:
        if list1.data < list2.data:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        else:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
    if list1 :
        curr.next = list1
    else:
        curr.next = list2
    return prev.next    
            
def mergeSort(head):
    # code here
    if head is None or head.next  is None:
        return head
    middle = getmiddle(head)
    right = middle.next
    middle.next = None
    left = head
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left,right)

def print__ll(head):
    curr = head
    while curr:
        print(curr.data, end =" ")
        if curr.next is not None:
            print("->", end=" ")
        curr = curr.next    
mergeSort(n1)
print__ll(n1)