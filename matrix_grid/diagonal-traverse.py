"""
https://leetcode.com/problems/diagonal-traverse/
"""

from collections import defaultdict
#OWN
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = defaultdict(list)
        visited = set()
        row_l, col_l = len(mat), len(mat[0])
        def dfs(row, col, level):
            nonlocal result
            if col < col_l and row < row_l:
                if (row, col) not in visited:
                    result[level].append(mat[row][col])
                    visited.add((row, col))
                    dfs(row, col + 1, level + 1)
                    dfs(row + 1, col, level + 1)
        dfs(0, 0, 0)
        final = []
        ind = 0
        while ind in result:
            if ind % 2 == 0:
                final += result[ind][::-1]
            else:
                final += result[ind]
            ind += 1
        return final


 public int[] findDiagonalOrder(int[][] matrix) {
        if (matrix.length == 0) return new int[0];
        int r = 0, c = 0, m = matrix.length, n = matrix[0].length, arr[] = new int[m * n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = matrix[r][c];
            if ((r + c) % 2 == 0) { // moving up
                if      (c == n - 1) { r++; }
                else if (r == 0)     { c++; }
                else            { r--; c++; }
            } else {                // moving down
                if      (r == m - 1) { c++; }
                else if (c == 0)     { r++; }
                else            { r++; c--; }
            }   
        }   
        return arr;
    }

public class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return new int[0];
        int m = matrix.length, n = matrix[0].length;
        
        int[] result = new int[m * n];
        int row = 0, col = 0, d = 1;

        for (int i = 0; i < m * n; i++) {
            result[i] = matrix[row][col];
            row -= d;
            col += d;
            
            if (row >= m) { row = m - 1; col += 2; d = -d;}
            if (col >= n) { col = n - 1; row += 2; d = -d;}
            if (row < 0)  { row = 0; d = -d;}
            if (col < 0)  { col = 0; d = -d;}
        }
        
        return result;
    }
}    