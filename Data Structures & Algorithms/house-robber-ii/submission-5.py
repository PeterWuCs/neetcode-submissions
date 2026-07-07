class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.simple_rob(nums[1:]), self.simple_rob(nums[:-1]))


    def simple_rob(self, nums):
        rob1, rob2  = 0, 0

        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return max(rob2, rob1)