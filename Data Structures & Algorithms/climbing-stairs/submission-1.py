class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2:2}
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for i in range(3, n+ 1):
            memo[i] = memo[i-2] + memo[i-1]

        return memo[n]