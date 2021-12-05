"""
https://www.interviewbit.com/old/problems/covered-uncovered-nodes/
"""
import collections

class Solution:
    def coveredNodes(self, A):
        cov = 0
        uncov = 0
        queue = collections.deque()
        queue.append(A)
        while queue:
            queue_size = len(queue)
            for index in range(queue_size):
                node = queue.popleft()
                if index == 0 or (index == queue_size - 1):
                    uncov += node.val
                else:
                    cov += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)                    
        return abs(cov - uncov)


class newNode:

	def Sum(t):
		if (t == None):
			return 0
		return t.key + Sum(t.left) + Sum(t.right)

	def uncoveredSumLeft(t):
		if (t.left == None and t.right == None):
			return t.key
		if (t.left != None):
			return t.key + uncoveredSumLeft(t.left)
		else:
			return t.key + uncoveredSumLeft(t.right)


	def uncoveredSumRight(t):
		if (t.left == None and t.right == None):
			return t.key
		if (t.right != None):
			return t.key + uncoveredSumRight(t.right)
		else:
			return t.key + uncoveredSumRight(t.left)

	def uncoverSum(t):
		lb = 0
		rb = 0
		if (t.left != None):
			lb = uncoveredSumLeft(t.left)
		if (t.right != None):
			rb = uncoveredSumRight(t.right)
		return t.key + lb + rb

	def isSumSame(root):
		sumUC = uncoverSum(root)
		sumT = Sum(root)
		return (sumUC == (sumT - sumUC))