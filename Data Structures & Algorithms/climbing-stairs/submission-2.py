class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n + 1):
            for j in range(1, 3):
                subproblem = i - j
                if subproblem <= 0:
                    continue
                
                memo[i] += memo[subproblem]

        return memo[n]