class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        nums = nums[:]
        num = nums.pop()

        a = self.subsets(nums)

        b = self.subsets(nums)


        for i in range(len(a)):
            a[i].append(num)
            b.append(a[i])

        return b
        