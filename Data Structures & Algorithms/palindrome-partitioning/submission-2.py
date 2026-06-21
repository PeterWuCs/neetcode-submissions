class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        temp = []

        def dfs(i):
            if i >= len(s):
                res.append(temp.copy())
                return

            for j in range(1, len(s) - i + 1):
                new = s[i : i + j]
                if new == new[: : -1]:
                    temp.append(new)
                    dfs(i + j)
                    temp.pop()

        dfs(0)
        return res        