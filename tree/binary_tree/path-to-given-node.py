"""
https://www.interviewbit.com/old/problems/path-to-given-node/
"""

  def solve(self, A, B):
        ans = []

        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
            if ans[-1] == B:
                return
            else:
                ans.pop()

        dfs(A)
        return ans