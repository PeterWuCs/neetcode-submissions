class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def factorial(n):
            res = 1
            for i in range(1, n + 1):
                res *= i

            return res

        
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)