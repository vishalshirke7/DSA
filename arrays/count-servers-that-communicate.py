"""
https://leetcode.com/problems/count-servers-that-communicate/
"""


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        answer = 0
        rows, columns = len(grid) * [0], len(grid[0]) * [0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows[row] += 1
                    columns[col] += 1
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (rows[row] > 1 or columns[col] > 1):
                    answer += 1
        return answer       


"""
public int countServers(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
    int numRows = grid.length;
    int numCols = grid[0].length;
    int rowCount[] = new int[numRows];
    int colCount[] = new int[numCols];
    int totalServers = 0;
    for (int row = 0; row < numRows; row++) {
        for (int col = 0; col < numCols; col++) {
            if (grid[row][col] == 1) {
                rowCount[row]++;
                colCount[col]++;
                totalServers++;
            }
        }
    }
    for (int row = 0; row < numRows; row++) {
        for (int col = 0; col < numCols; col++) {
            if (grid[row][col] == 1) {
                if (rowCount[row] == 1 && colCount[col] == 1) {
                    totalServers--;
                }
            }
        }
    }
    return totalServers;
}
"""        