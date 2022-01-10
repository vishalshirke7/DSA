"""
https://leetcode.com/problems/number-of-islands/
"""

# TC - O(M * N)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col):
            if grid[row][col] == "1":
                grid[row][col] = "2"
                if row >= 1:
                    dfs(row - 1, col)
                if row + 1 < rows:
                    dfs(row + 1, col)
                if col >= 1:
                    dfs(row, col - 1)
                if col + 1 < cols:
                    dfs(row, col + 1)                    
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        return islands