def uniquePathsWithObstacles(obstacleGrid: list[list[int]]):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    path = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        path[0][i] = 1
    for j in range(m):
        if obstacleGrid[j][0] == 1:
            break
        path[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if not obstacleGrid[i][j]:
                path[i][j] = path[i - 1][j] + path[i][j - 1]
    return path[m - 1][n - 1]


obstacleGrid = [[0, 1], [0, 0]]
uniquePathsWithObstacles(obstacleGrid)
