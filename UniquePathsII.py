class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        if obstacleGrid[row-1][col-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        for i in range(row):
            for j in range(col):
                if (i == 0 and j == 0):
                    obstacleGrid[i][j] = 1
                elif (obstacleGrid[i][j] == 1): #update obstacle
                    obstacleGrid[i][j] = 0

                elif (i > 0 and j > 0): #for cases when top and left side are open paths
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                elif (i > 0): #for cases when top side is open and no left side
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else: #for cases when left side is open and no top side
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                print(obstacleGrid[i][j])
        return obstacleGrid[row-1][col-1]
