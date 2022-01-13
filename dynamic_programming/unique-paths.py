"""
https://leetcode.com/problems/unique-paths/
"""
# Brute force time complexity - 2 ^ (m+n)

# OWN (DP) O(m * n)
# TOP DOWN - memoization

class Solution:
    def uniquePaths(self, m, n):
        def dfs(c_row, c_col, matrix):
            if c_row == m - 1 and c_col == n - 1:
                return 1
            l, r = 0, 0
            if matrix[c_row][c_col] > 0:
                return matrix[c_row][c_col]
            if c_row + 1 < m:
                l = dfs(c_row + 1, c_col, matrix)
            if c_col + 1 < n:
                r = dfs(c_row, c_col + 1, matrix)
            matrix[c_row][c_col] = l + r
            return matrix[c_row][c_col]
        matrix = [[0 for j in range(n)]for i in range(m)]
        return dfs(0, 0, matrix)


# BOTTOM UP - ITERATIVE - TABULATION