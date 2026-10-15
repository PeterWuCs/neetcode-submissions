class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        return self.b_search(low, high, nums, target)


    def b_search(self, low, high, nums, target):

        if low > high:
            return - 1
        mid = (low + high) //2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            return self.b_search(low, mid - 1, nums, target)
        return self.b_search(mid + 1, high, nums, target)
