class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        first = nums[0]
        second = nums[1]
        third = nums[2] + first

        for i in range(3, len(nums)):
            temp = third
            third = max(first, second) + nums[i]
            first = second
            second = temp
            
        return max(second, third)
            
        