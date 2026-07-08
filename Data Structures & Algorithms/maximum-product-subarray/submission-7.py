class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[-1]

        prod = nums[0]
        larggest = max(nums)

        for i in range(1, n):
            num = nums[i]
            if num == 0 or prod == 0:
                prod = num
            else:
                prod = num * prod
            larggest = max(larggest, prod)

        prod = nums[n - 1]
        for i in range(n - 2, -1, - 1):
            num = nums[i]
            if num == 0 or prod == 0:
                prod = num
            else:
                prod = num * prod
            larggest = max(larggest, prod)



        return larggest


