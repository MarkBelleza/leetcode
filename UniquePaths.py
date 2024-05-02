class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m
        col = n
        grid = Solution.create_grid(row, col)

        for i in range(row):
  
            for j in range(col):
                if (i == 0 and j == 0):
                    grid[i][j] = 1

                elif (i > 0 and j > 0): #for cases when top and left side are open paths
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                elif (i > 0): #for cases when top side is open and no left side
                    grid[i][j] = grid[i-1][j]
                else: #for cases when left side is open and no top side
                    grid[i][j] = grid[i][j-1]
            

        return grid[row-1][col-1]
    
    def create_grid(m, n):
        grid = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)  # You can initialize elements with any value you want
            grid.append(row)
        return grid
