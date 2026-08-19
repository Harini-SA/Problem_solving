def __init__(self):
        self.stack = []

def push(self, x):
    if not self.stack:
        self.stack.append([x,x])
    else:    
        current_min = self.stack[-1][1]
        new_min = min(x,current_min)
        self.stack.append([x,new_min])

def pop(self):
    if not self.stack:
        return -1
    self.stack.pop()    
   
def peek(self):
    if not self.stack:
        return -1
    return self.stack[-1][0]    
    
def isEmpty(self):
    if not self.stack:
        return True
    return False    
   
def getMin(self):
    if not self.stack:
        return -1
    return self.stack[-1][1]