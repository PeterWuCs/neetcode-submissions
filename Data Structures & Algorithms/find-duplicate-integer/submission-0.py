class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first = nums[0]
        while True:
            if first == nums[first]:
                return first
            temp = first
            first = nums[temp]
            nums[temp] = 0
            if first == 0:
                return temp