class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 4

                    if i - 1 >= 0 and grid[i-1][j] == 1: #Top
                        ans -= 1
                    if i + 1 < len(grid) and grid[i+1][j] == 1: #Bottom
                        ans -= 1
                    if j - 1 >= 0 and grid[i][j-1] == 1: #Left
                        ans -= 1
                    if j + 1 < len(grid[0]) and grid[i][j+1] == 1: #Right
                        ans -= 1
        return ans

        # Time: O(n*m)
        # Space: O(1)
