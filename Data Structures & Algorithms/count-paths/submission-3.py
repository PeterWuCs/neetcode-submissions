class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

        for i in range(m):
            dp[i][n - 1] = 1
        for i in range(n):
            dp[m-1][i] = 1

        def helper(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = helper(i + 1, j) + helper(i, j + 1)
            return dp[i][j]


        return helper(0, 0)

