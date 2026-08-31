class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, x):
        newnode = Node(x)
        if self.front is None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front= self.front.next
        return temp

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.front.data    

    def size(self):
        length = 0
        size = self.front
        while size != None:
            length += 1
            size = size.next
        return length    

