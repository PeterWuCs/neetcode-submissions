class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0


        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] > len(nums):
                continue

            if nums[i] > 0:
                index = nums[i] - 1
            else:
                index = nums[i] * (-1) - 1
            
            if nums[index] == 0:
                nums[index] = len(nums) + 1
            elif nums[index] > 0:
                nums[index] = nums[index] * (-1)
        
        print(nums)

        for i in range(len(nums)):
            if nums[i] == 0 or 0 <= nums[i] <= len(nums):
                return i + 1
        
        return len(nums) + 1
