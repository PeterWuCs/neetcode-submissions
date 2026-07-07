class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        zero = cost[0]
        one = cost[1]

        for i in range(2, len(cost)):
            temp = one
            one = min(zero, one) + cost[i]
            zero = temp

        return min(one, zero)

