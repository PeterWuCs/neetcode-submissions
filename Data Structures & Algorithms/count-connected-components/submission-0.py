class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()

        g = defaultdict(list)

        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        

        def dfs(i):

            if i in visited:
                return

            visited.add(i)

            for v in g[i]:
                dfs(v)

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count

        