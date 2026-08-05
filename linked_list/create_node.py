class Node:
    def __init__(self,data):
        self.data = data
        self.next =None
n1 =Node(5)
n2 = Node(10)
n1.next = n2
current = n1
while current:
    print(current.data)
    current = current.next        