class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(int)
        memo[(0, 0)] = 1

        for i in range(len(nums)):
            new_memo = defaultdict(int)
            for key in memo:
                index = key[0]
                cur_sum = key[1]

                new_memo[(index + 1, cur_sum + nums[i])] += memo[key]
                new_memo[(index + 1, cur_sum - nums[i])] += memo[key]
            memo = new_memo


        return memo[(len(nums), target)]