class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threashold = n // 3

        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
                continue

            count_dict[num] = 1
            if len(count_dict) <= 2:
                continue
            
            del_set = []
            for key in count_dict:
                count_dict[key] = count_dict[key] - 1
                if count_dict[key] == 0:
                    del_set.append(key)

            for to_remove in del_set:
                del count_dict[to_remove]
            
        res = []


        for key in count_dict:
            if nums.count(key) > threashold:
                res.append(key)

        return res
        