class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        threashold = n // 3

        count_dict = {}
        for i in range(n):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
            else:
                
                count_dict[nums[i]] = 1

        res = []

        for key in count_dict:
            if count_dict[key] > threashold:
                res.append(key)

        return res
        