class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = [-1] * (amount + 1)
        memo[0] = 0
    
        for i in range(1, amount + 1):
            for coin in coins:
                subproblem = i - coin
                print(subproblem)
                if subproblem < 0:
                    continue
                if subproblem == 0:
                    memo[i] = 1
                    break
                    
                if memo[subproblem] != -1:
                    if memo[i] == -1:
                        memo[i] = memo[subproblem] + 1
                    else:
                        memo[i] = min(memo[subproblem] + 1, memo[i])
                     
                    
        print(memo)
        return memo[-1]