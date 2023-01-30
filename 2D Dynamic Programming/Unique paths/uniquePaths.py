def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0 for i in range(n)] for j in range(m)]
    # print(len(dp), len(dp[0]))
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[i][j] = 1
            if i+1 < m:
                dp[i][j] += dp[i+1][j]
            if j+1 < n:
                dp[i][j] += dp[i][j+1]
    return dp[0][0]
