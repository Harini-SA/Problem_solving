class myQueue:
    def __init__(self, n):
        self.n = n
        self.size = 0
        self.arr = [0]*n
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.size == 0
        
    def isFull(self):
        return self.size == self.n
        
    def enqueue(self, x):
        if self.size == self.n:
            return -1
        self.arr[self.rear % self.n] = x
        self.rear += 1
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        self.arr[self.front % self.n] = 0
        self.front += 1
        self.size -= 1

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front% self.n]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[(self.rear-1) % self.n]
q1 = myQueue(5)
print(q1.enqueue(5))
print(q1.dequeue())
print(q1.isEmpty()) 
print(q1.isFull())
print(q1.getFront())
print(q1.getRear())   
        
        