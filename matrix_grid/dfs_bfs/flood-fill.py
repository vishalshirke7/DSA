"""
https://leetcode.com/problems/flood-fill/
"""

# Time Complexity: O(N)O(N), where NN is the number of pixels in the image. We might process every pixel.

# Space Complexity: O(N)O(N), the size of the implicit call stack when calling dfs

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(row, col):
            if image[row][col] == color:
                image[row][col] = newColor
                if row + 1 < rows:
                    dfs(row + 1, col)
                if row >= 1:
                    dfs(row - 1, col)
                if col + 1 < cols:
                    dfs(row, col + 1)
                if col >= 1:
                    dfs(row, col - 1)
        dfs(sr, sc)
        return image


