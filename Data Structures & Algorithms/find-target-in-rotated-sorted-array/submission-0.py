class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r, target):
            while l <= r:
                middle = (l + r) // 2

                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1

            return -1


        l, r = 0, len(nums) - 1

        pivot = -1
        print("help1")
        while l < r:
            middle = (l + r) // 2

            test = middle + 1
            if middle + 1 == len(nums):
                test = 0
            if nums[test] < nums[middle]:
                pivot = test
                break

            if nums[r] < nums[middle]:
                l = middle 
            else:
                r = middle
        print("heelp")
        if pivot == -1:
            pivot = l
        
        if pivot == 0:
            return binary_search(0, len(nums) - 1, target)

        res_one = binary_search(0, pivot, target)
        res_two = binary_search(pivot, len(nums) - 1, target)
        
        if res_one == -1:
            return res_two
        return res_one
    