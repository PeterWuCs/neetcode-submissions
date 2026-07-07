class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        one = 2
        two = 1

        for i in range(3, n + 1):
            temp = one
            one = two + one
            two = temp

        return one