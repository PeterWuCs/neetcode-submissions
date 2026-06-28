class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse= True)

        print(tickets)
        g = defaultdict(list)

        for src, dst in tickets:
            g[src].append(dst)

        ans = []
        
        def dfs(i):
            if len(g[i]) == 0:
                ans.append(i)
                return
            
            while len(g[i]) != 0:
                new = g[i].pop()
                dfs(new)

            ans.append(i)

        dfs("JFK")

        ans.reverse()
        return ans


