"""
https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
"""

"https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/328847/Python-Greedy-O(n)-with-clarification-and-analysis"

def maxDepthAfterSplit(seq):
    total = 0
    for char in seq:
        if char == '(':
            total += 1
    min_depth = total // 2
    output = [1] * len(seq)
    op, close = 0, 0
    total_op, total_close = 0, 0 
    for index, char in enumerate(seq):
        if char == '(':
            total_op += 1
            if op != min_depth:
                op += 1
                output[index] = 0
        elif char == ')':
            total_close += 1
            if close != min_depth and total_close >= total_op:
                output[index] = 0
                close += 1
            else:
                total_op -= 1
        if op == close == min_depth:
            break
    return output
            

# print('Output', maxDepthAfterSplit("(()())"))
# print('Output', maxDepthAfterSplit("((()()))"))
print('Output', maxDepthAfterSplit("(((()))((())))"))
