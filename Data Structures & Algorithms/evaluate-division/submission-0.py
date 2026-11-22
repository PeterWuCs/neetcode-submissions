class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for i in range((len(equations))):
            a = equations[i][0]
            b = equations[i][1]
            c = values[i]


            graph[a].append((b, c))
            graph[b].append((a, 1 / c))

        visited = set()

        def dfs(target, node):

            if node in visited:
                return 0

            
            if target == node:
                return 1
            
            visited.add(node)
            for v, w in graph[node]:
                res = dfs(target, v)
                if res != 0:
                    return 1 * w * res
            
            return 0

        res = []

        for i, j in queries:

            if len(graph[i]) == 0 or len(graph[j]) == 0:
                res.append(-1)
            else:
                num = dfs(j, i)
                if num == 0:
                    res.append(-1)

                else:
                    res.append(num)
                visited = set()

        return res






