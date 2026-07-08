class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        curMin, curMax = 1, 1
        larggest = max(nums)

        for num in nums:
            temp = curMax * num
            curMax = max(curMin * num, curMax * num, num)
            curMin = min(curMin * num, temp, num)
            larggest = max(larggest, curMax)

        return larggest


