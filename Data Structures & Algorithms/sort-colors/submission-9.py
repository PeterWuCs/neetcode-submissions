class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, i = 0, 0
        r = len(nums) - 1

        while i < len(nums) and i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
'''
i: 1
l: 0
r: 1

'''