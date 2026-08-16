class myStack:
    def __init__(self, n):
        self.capacity = n
        self.arr = [0] * self.capacity
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False    
       
    def isFull(self):
        if self.top == self.capacity -1:
            return True
        return False    

    def push(self, x):
        if self.top == self.capacity -1:
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            return -1
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top != -1:
            return self.arr[self.top]
        return self.top  