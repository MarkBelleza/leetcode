class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                pass
            else:
                grid[i][j] = '0'
                dfs(i-1, j) #Top
                dfs(i+1, j) #Botton
                dfs(i, j-1) #Left
                dfs(i, j+1) #Right

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans

    # Time: O(n*m)
    # Space: O(n*m)
