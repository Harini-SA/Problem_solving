class TwoStacks:
    def __init__(self):
        self.size = 100
        self.arr = [0]* self.size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
    def push2(self, x):
        if self.top1 <self.top2 -1 :
            self.top2 -= 1
            self.arr[self.top2] = x
    def pop1(self):
        if self.top1 >-1:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        return -1   
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        return -1 