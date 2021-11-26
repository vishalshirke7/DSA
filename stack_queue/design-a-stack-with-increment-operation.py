"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = list()

    def push(self, x: int) -> None:
        if len(self.stack) <= self.maxSize - 1:
            self.stack.append(x)        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1
    
    def increment(self, k: int, val: int) -> None:
        size = len(self.stack)
        for index in range(min(size, k)):
            self.stack[index] += val
            
            
    #Better
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val    


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)