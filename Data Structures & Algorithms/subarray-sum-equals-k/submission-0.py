class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_dict = defaultdict(int)
        count_dict[0] = 1
        res = 0

        cur_sum = 0
        for num in nums:

            cur_sum += num

            diff = cur_sum - k

            res += count_dict[ diff ]

            count_dict[cur_sum] += 1


        return res