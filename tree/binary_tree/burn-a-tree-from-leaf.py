"""
https://www.interviewbit.com/old/problems/burn-a-tree/
"""
import sys
sys.setrecursionlimit(10**4)
        
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        def bottom_up(node, starting):
            if not node: return -1, False

            if node.val == starting: return 0, True

            time_left, burn_left = bottom_up(node.left, starting)
            time_right, burn_right = bottom_up(node.right, starting)

            burn = burn_left or burn_right
            if not burn: time = max(time_left, time_right)
            else:
                curr = time_left + time_right + 2
                if self.time < curr: self.time = curr
                time = time_left if burn_left else time_right

            return time + 1, burn

        self.time = 0
        bottom_up(A, B)
        return self.time
