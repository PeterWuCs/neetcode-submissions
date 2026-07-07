class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0

        for num in nums:
            temp = second
            second = max(first + num, second)
            first = temp


        return max(first, second)
        