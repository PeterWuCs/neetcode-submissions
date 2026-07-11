class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        row = [0] * m
        dp = [row.copy() for _ in range(n)]

        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, n):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0] 
                
        for j in range(1, m):
            print(j)
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n - 1][m - 1]


