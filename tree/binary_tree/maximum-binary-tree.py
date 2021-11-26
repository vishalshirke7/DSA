"""https://leetcode.com/problems/maximum-binary-tree/"""
"""
Complexity Analysis

Time complexity : O(n^2) 
The function construct is called nn times. At each level of the recursive tree, we traverse over all the nn elements to find the maximum element. 
In the average case, there will be a \log nlogn levels leading to a complexity of O\big(n\log n\big)O(nlogn). 
In the worst case, the depth of the recursive tree can grow upto nn, which happens in the case of a sorted numsnums array,
 giving a complexity of O(n^2)O(n 
Space complexity : O(n)O(n). The size of the setset can grow upto nn in the worst case. 
In the average case, the size will be \log nlogn for nn elements in numsnums, giving an average case complexity of O(\log n)O(logn)
"""

#OWN
class Solution:

    def get_max(self, nums):
        maximum = 0
        for index in range(len(nums)):
            if nums[index] > nums[maximum]:
                maximum = index
        return maximum
    
    def buildTree(self, nums):
        if not nums:
            return None
        cur_max = self.get_max(nums)
        node = TreeNode(nums[cur_max])
        node.left = self.buildTree(nums[:cur_max])
        node.right = self.buildTree(nums[cur_max + 1:])
        return node
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums)



#2. Stack with O(n)
class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = list()
        for val in nums:
            node = TreeNode(val)
            while stack and stack[-1] < val:
                node.left = stack[-1]
                stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

