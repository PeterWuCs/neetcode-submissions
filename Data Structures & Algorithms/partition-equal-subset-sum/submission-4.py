class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        
        memo = {}
        def dp(target, index):
            if index == len(nums):
                return False
            if target == nums[index]:
                return True
            if (target, index) in memo:
                return memo[(target, index)]

            if target > nums[index]:
                memo[(target, index)] = dp(target - nums[index], index + 1) or dp(target, index + 1)
            else:
                memo[(target, index)] = dp(target, index + 1)
                
            return memo[(target, index)]

        return dp(target, 0)