class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        n = len(nums)
        k = k % n

        
        while k:
            lasttt_num = nums[n - 1]

            last_num = nums[0]
            for i in range(1, n):
                temp = nums[i]
                nums[i] = last_num
                last_num = temp

            nums[0] = lasttt_num

            k -= 1

    



