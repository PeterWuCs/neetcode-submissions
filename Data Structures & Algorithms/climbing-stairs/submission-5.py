class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 0:
            return 0
        one = 2
        two = 1

        for i in range(3, n + 1):
            temp = one
            one = two + one
            two = temp

        return one