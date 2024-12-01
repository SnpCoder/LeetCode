def minPathSum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    path_cost = [[0 for _ in range(n)] for _ in range(m)]
    path_cost[0][0] = grid[0][0]
    for i in range(1, n):
        path_cost[0][i] = path_cost[0][i - 1] + grid[0][i]
    for j in range(1, m):
        path_cost[j][0] = path_cost[j - 1][0] + grid[j][0]
    for i in range(1, m):
        for j in range(1, n):
            path_cost[i][j] = min(path_cost[i - 1][j], path_cost[i][j - 1]) + grid[i][j]
    return path_cost[m - 1][n - 1]
