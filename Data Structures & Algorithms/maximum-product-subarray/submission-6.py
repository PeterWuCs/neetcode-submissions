class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[-1]

        prod = [-1] * n
        prod[0] = nums[0]

        for i in range(1, n):
            num = nums[i]
            if num == 0 or prod[i - 1] == 0:
                prod[i] = num
            else:
                prod[i] = num * prod[i - 1]

        sprod = [-1] * n
        sprod[-1] = nums[-1]

        for i in range(n - 2, -1, - 1):
            num = nums[i]
            if num == 0 or sprod[i + 1] == 0:
                sprod[i] = num
            else:
                sprod[i] = num * sprod[i + 1]



        return max(max(prod), max(sprod))


