class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = nums[0]
        
        if sum >= target:
            return 1

        shortest = len(nums) + 1

        l = 0
        for r in range(1, len(nums)):
            sum += nums[r]

            while sum >= target and l <= r:
                shortest = min(shortest, r - l + 1)
                sum -= nums[l]
                l += 1
        
        if shortest == len(nums) + 1:
            return 0
        return shortest