obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0,0],[1,1],[0,0]]
obstacleGrid = [[0]]

m = len(obstacleGrid)
n = len(obstacleGrid[0])
dp = [[0 for _ in range(n)] for _ in range(m)]
if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
    print(0)
dp[0][0] = 1
for i in range(1, m):
    if obstacleGrid[i][0] == 0:
        dp[i][0] = 1
    else:
        break
for j in range(1, n):
    if obstacleGrid[0][j] == 0:
        dp[0][j] = 1
    else:
        break
print(dp)
for i in range(1, m):
    for j in range(1, n):
        if obstacleGrid[i][j] == 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = 0
print(dp[m - 1][n - 1])
