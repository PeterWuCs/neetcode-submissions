class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target + 1)
        memo[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    j = i - num
                    if memo[j] >= 1:
                        memo[i] += memo[j]

        return memo[-1]