class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n

        for i, num in enumerate(nums):
            longest = 0
            for j in range(i):
                if nums[j] < num:
                    longest = max(longest, memo[j])
            memo[i] = longest + 1

        return max(memo)
        
