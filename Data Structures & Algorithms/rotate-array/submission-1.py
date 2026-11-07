class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        n = len(nums)
        k = k % n

        
        nums.reverse()

        l = 0 
        r = k - 1

        while r > l:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = k 
        r = n - 1
        
        while r > l:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        




