class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        result = []
        temp = []
        def dfs(i, sum):
            if sum > target:
                return
            if sum == target:
                result.append(temp[:])
                return
            
            if i >= len(nums):
                return
            
            temp.append(nums[i])
            dfs(i, sum + nums[i])
            temp.pop()
            dfs(i + 1, sum)
            
        dfs(0, 0)
        return result


