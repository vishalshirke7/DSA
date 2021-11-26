"""
https://leetcode.com/problems/min-stack/
https://www.interviewbit.com/old/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        self.stack = list()
        
    def push(self, val: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or val < cur_min:
            cur_min = val
        self.stack.append((cur_min, val))

    def pop(self) -> None:
        self.stack.pop()
                
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None


class MinStack:
    # @param x, an integer
    
    
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            self.minStack.append(x)
            

    # @return nothing
    def pop(self):
        
        if len(self.stack) == 0:
            return
        
        x = self.stack[-1]
        self.stack.pop()
        
        if x == self.minStack[-1]:
            self.minStack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.minStack) == 0:
            return -1
        return self.minStack[-1]

        