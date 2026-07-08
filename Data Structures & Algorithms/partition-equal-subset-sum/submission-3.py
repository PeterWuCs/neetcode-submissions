class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2:
            return False

        target = total // 2
        memo = [0] * (target + 1)
        memo[0] = 1

        for i, num in enumerate(nums):
            if num > target:
                return False
            if num == target:
                return True
            change = set()
            change.add(num)

            for j in range(1, target + 1):
                if memo[j] == 1 and j + num <= target:
                    change.add(j + num)
            for k in change:
                memo[k] = 1

        return memo[target] == 1