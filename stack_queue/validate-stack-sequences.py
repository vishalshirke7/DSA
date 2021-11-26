"""
https://leetcode.com/problems/validate-stack-sequences/
"""

def validateStackSequences(pushed, popped):
        size = len(pushed)
        ptr1, ptr2, stack = 1, 0, [pushed[0]]
        while stack:
            if stack[-1] == popped[ptr2]:
                ptr2 += 1
                stack.pop()
                if not stack and ptr1 < size:
                    stack.append(pushed[ptr1])
                    ptr1 += 1
            else:
                if ptr1 >= size:
                    return False
                stack.append(pushed[ptr1])
                ptr1 += 1
        return True


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
        
print('Output', validateStackSequences([4,0,1,2,3],[4,2,3,0,1]))