class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []

        candidates.sort()

        def dfs(i, sum):
            if sum == target:
                res.append(temp[:])
                return
            
            elif len(candidates) <= i or sum > target:
                return
            
            else:
                temp.append(candidates[i])
                dfs(i + 1, sum + candidates[i])
                
                i += 1
                if i < len(candidates) and candidates[i] == candidates[i - 1]:
                    while i < len(candidates):
                        if candidates[i] != candidates[i - 1]:
                            break
                        i += 1
                temp.pop()
                dfs(i, sum)

        dfs(0, 0)
        return res
