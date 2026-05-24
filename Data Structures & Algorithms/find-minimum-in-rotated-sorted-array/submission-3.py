class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            test = middle + 1
            if middle + 1 == len(nums):
                test = 0
            if nums[test] < nums[middle]:
                return nums[test]

            if nums[r] < nums[middle]:
                l = middle 
            else:
                r = middle
        
        return nums[l]