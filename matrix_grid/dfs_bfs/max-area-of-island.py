"""
https://leetcode.com/problems/max-area-of-island/
"""

# OWN

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col):
            if grid[row][col] == 1:
                grid[row][col] = 0
                up, do, le, ri = 0, 0, 0, 0
                if row + 1 < rows:
                    do = dfs(row + 1, col)
                if row >= 1:
                    up = dfs(row - 1, col)
                if col + 1 < cols:
                    ri = dfs(row, col + 1)
                if col >= 1:
                    le = dfs(row, col - 1)
                return 1 + up + do + le + ri
            return 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        return max_area