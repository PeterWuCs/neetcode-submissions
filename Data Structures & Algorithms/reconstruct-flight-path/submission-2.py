class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort(reverse= True)

        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        res = []
        
        def dfs(node):
            if len(graph[node]) == 0:
                res.append(node)
                return
            
            while len(graph[node]) != 0:
                last = graph[node].pop()
                dfs(last)
            res.append(node)

        dfs("JFK")
        res.reverse()

        return res