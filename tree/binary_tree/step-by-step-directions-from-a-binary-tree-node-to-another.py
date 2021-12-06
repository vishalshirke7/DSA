"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
"""

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        ans = []
        def find_path(root, target):
            nonlocal ans
            if not root:
                return False
            if root.val == target:
                return True
            if find_path(root.left, target):
                ans.append('L')
                return True
            if find_path(root.right, target):
                ans.append('R')
                return True
            return False
        
        find_path(root, startValue)
        startPath = ans
        ans = []
        find_path(root, destValue)
        endPath = ans
        while len(startPath) > 0 and len(endPath) > 0 and startPath[-1] == endPath[-1]:
            startPath.pop()
            endPath.pop()
        temp = ""
        for i in range(len(startPath)):
            temp += "U"
        endPath = endPath[::-1]
        return "".join(temp) + "".join(endPath)