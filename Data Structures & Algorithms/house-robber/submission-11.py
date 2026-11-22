class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        res = nums[0]
        res_two = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res = max(res + nums[i], res_two)
            res_two, res = res, res_two

        return max(res, res_two)
