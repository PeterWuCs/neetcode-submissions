class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_a = {}

        for i in range(len(nums)):

            dict_a[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in dict_a and dict_a[nums[i]] != i:

                return [ min(dict_a[nums[i]], i), max(dict_a[nums[i]], i)]