class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 3:
            return 2
        if n == 2:
            return 1
        memo = [0] * (n + 1)

        memo[1] = 1
        memo[2] = 2
        memo[3] = 3

        for i in range(4, n + 1):
            for j in range(2, i):
                num = i - j
                memo[i] = max(memo[i], memo[num] * memo[j])

        return memo[-1]
