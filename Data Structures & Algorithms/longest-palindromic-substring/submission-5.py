class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]

        start = 0
        longest = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if longest < j - i + 1:
                        longest = j - i + 1
                        start = i
        
        return s[start : start + longest]