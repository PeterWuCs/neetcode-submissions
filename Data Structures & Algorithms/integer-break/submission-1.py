class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        memo = {}
        memo[2] = 2
        memo[1] = 1
        memo[3] = 3

        def helper(n):
            if n in memo:
                return memo[n]
            
            largest = 2 * (n - 2)
            for i in range(3, n - 2):
                j = n - i
                largest = max(largest, helper(i) * helper(j))

            memo[n] = largest

            return memo[n]
        helper(n)
        return memo[n]