"""
https://leetcode.com/problems/find-all-groups-of-farmland/
"""

# OWN
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = list()
        rows, cols = len(land), len(land[0])
        
        def dfs(row, col):
            if land[row][col] == 1:
                right_row, down_row, right_col, down_col = -1, -1, -1, -1
                land[row][col] = 0
                if row + 1 < rows:
                    down_row, down_col = dfs(row + 1, col)
                if col + 1 < cols:
                    right_row, right_col = dfs(row, col + 1)                    
                return max(row, right_row, down_row), max(col, right_col, down_col)
            return -1, -1
        
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1:
                    far_row, far_col = dfs(row, col)
                    if far_row != -1 and far_col != -1:
                        result.append([row,col,far_row,far_col])
        return result

# NON DFS

"""
class Solution {
        public:
            vector<vector<int>> findFarmland(vector<vector<int>>& land) {
                int m = land.size();
                int n = land[0].size();
                
                vector<vector<int>> result;
                for(int i = 0; i<m; i++) {
                    for(int j = 0; j<n; j++) {
                        
                        //We have to deal with 1s only
                        if(land[i][j] == 0) continue;
        
                        //Find right most column of rectangle (see the image below)
                        int c1 = j;
                        while(c1 < n && land[i][c1] == 1) {
                            c1++;
                        }
        
                        //Find bottom most row of rectangle (see the image below)
                        int r2 = i;
                        while(r2 < m && land[r2][j] == 1) {
                            r2++;
                        }
                        
                        //Then you can find bottom right most of rectangle
                        c1 = c1==0 ? c1 : c1-1;
                        r2 = r2==0 ? r2 : r2-1;
        
                        //Use them as your answer
                        //{r1, c1} = {i, j}
                        //{r2, c2} = {r2, c1}
                        result.push_back({i, j, r2, c1});
                        
                        //Now, mark the covered land with 0 so that you don't consider them later
                        for(int k = i; k<=r2; k++) {
                            for(int l = j; l<=c1; l++) {
                                land[k][l] = 0;
                            }
                        }
                        
                    }
                }
                return result;
            }
        };
"""        