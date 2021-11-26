"""
https://leetcode.com/problems/daily-temperatures/
"""

def dailyTemperatures(temperatures):
    stack = list()
    if not temperatures:
        return []
    stack.append((0, temperatures[0]))
    op = [0] * len(temperatures)
    for index in range(1, len(temperatures)):
        while stack and temperatures[index] > stack[-1][1]:
            op[stack[-1][0]] = index - stack[-1][0]
            stack.pop()
        stack.append((index, temperatures[index]))
    return op


print('Output', dailyTemperatures([73,74,75,71,69,72,76,73]))
print('Output', dailyTemperatures([30,40,50,60]))
print('Output', dailyTemperatures([30,60,90]))