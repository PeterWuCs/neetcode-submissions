class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        
        possible = set()
        possible.add(0)

        for i in range(len(nums)):
            new_possible = set()
            for t in possible:
                if t + nums[i] == target:
                    return True
                if t + nums[i] < target:
                    new_possible.add(t + nums[i])

            possible |= new_possible

                    


        return target in possible