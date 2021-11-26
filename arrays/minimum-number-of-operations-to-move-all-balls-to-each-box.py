"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

"""

def minOperations(boxes):
    ans = [0]*len(boxes)
    leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
    for i in range(1, n):
        if boxes[i-1] == '1':
        	leftCount += 1
        leftCost += leftCount
        ans[i] = leftCost
    for i in range(n-2, -1, -1):
        if boxes[i+1] == '1':
        	rightCount += 1
        rightCost += rightCount
        ans[i] += rightCost
    return ans


def minOperations(boxes):
    n = len(boxes)
    answer = [0] * n
    curr, steps = 0, 0
    for i in range(n):
        answer[i] += steps
        curr += int(boxes[i])
        steps += curr
    curr, steps = 0, 0
    for i in reversed(range(n)):
        answer[i] += steps
        curr += int(boxes[i])
        steps += curr
    return answer

print(minOperations("110"))
print(minOperations("001011"))
