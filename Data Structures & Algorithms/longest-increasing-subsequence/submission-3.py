class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n

        for i in range(1, n):
            longest = -1
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    longest = max(longest, memo[j])
                
            if longest != -1:
                memo[i] = longest + 1


        return max(memo) 
