class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        leaves = deque()

        edge_count = {}

        for u in graph:
            edge_count[u] = len(graph[u])
            if edge_count[u] == 1:
                leaves.append(u)

        
        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in graph[node]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 1:
                        leaves.append(nei)

        



                