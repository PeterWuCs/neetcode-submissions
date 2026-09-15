class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            elif nums[i] == 1:
                one_count += 1
            else:
                two_count += 1

        for i in range(len(nums)):
            if zero_count != 0:
                nums[i] = 0
                zero_count -= 1
            elif one_count != 0:
                nums[i] = 1
                one_count -= 1
            else:
                nums[i] = 2
                two_count -= 1
        

        