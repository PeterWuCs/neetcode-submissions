class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        
        res_zero = 0
        res_one = 1
        res_two = 1

        for _ in range(3, n + 1):
            newest = res_zero + res_one + res_two
            res_zero = res_one
            res_one = res_two
            res_two = newest

        return res_two
