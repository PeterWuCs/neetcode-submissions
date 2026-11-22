class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')

        pos = 1
        neg = 1

        for num in nums:
            if num != 0:
                temp = pos
                pos = max(pos * num, num, neg * num)
                neg = min(temp * num, num, neg * num)
                res = max(pos, neg, res)

            elif num == 0:
                res = max(num, res)
                pos = 1
                neg = 1

        return res
                