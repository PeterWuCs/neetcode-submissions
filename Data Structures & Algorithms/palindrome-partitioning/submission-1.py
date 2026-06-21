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
                    print(new)
                    print("rev", new[: : -1])
                    temp.append(new)
                    print(i + j)
                    dfs(i + j)
                    temp.remove(new)

        dfs(0)
        return res        