class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def helper(i, target):
            if i == len(nums):
                return 0
            if (i, target) in memo:
                return memo[(i, target)]

            if i == len(nums) - 1:
                res = 0
                if nums[i] == target:
                    res += 1
                if -nums[i] == target:
                    res += 1
                memo[(i, target)] = res
                return res

            memo[(i, target)] = helper(i + 1, target + nums[i]) + helper(i + 1, target - nums[i])
            return memo[(i, target)]
            
        return helper(0, target)