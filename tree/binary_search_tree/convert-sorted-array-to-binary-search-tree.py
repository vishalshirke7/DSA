"""
https://www.interviewbit.com/old/problems/sorted-array-to-balanced-bst/
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        def construct(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(A[mid])
            node.left = construct(left, mid - 1)
            node.right = construct(mid + 1, right)
            return node
        return construct(0, len(A) - 1)