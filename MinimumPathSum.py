class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid) 
        col = len(grid[0]) 

        for i in range(row):
            for j in range(col):

                down = float('inf')
                right = float('inf')

                if(i == 0 and j == 0): #skip this iteration
                    continue 

                if i != 0: #going down
                    down = grid[i][j] + grid[i-1][j]
                if j != 0: #going right
                    right = grid[i][j] + grid[i][j-1]
                
                grid[i][j] = min(down, right)
                print(grid[i][j])

        return grid[row-1][col-1] 
            
