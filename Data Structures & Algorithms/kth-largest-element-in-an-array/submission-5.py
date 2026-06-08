import sys
sys.setrecursionlimit(10**6)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        def quick(l, r):
            p = nums[r]

            pointer = l

            for i in range(l, r):
                if nums[i] < p:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            nums[pointer], nums[r] = nums[r], nums[pointer]

            if n - k > pointer:
                return quick(pointer + 1, r)
            elif n - k < pointer:
                return quick(l, pointer - 1)
            else:
                return nums[pointer]
        return quick(0, n - 1)
        