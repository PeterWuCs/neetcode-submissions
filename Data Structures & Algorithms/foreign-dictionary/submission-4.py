class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        g = defaultdict(list)
        source = ""


        for i in range(1, len(words)):
            j = 0   
            l1 = len(words[i - 1])
            l2 = len(words[i])

            valid = False
            while j < l1 and j < l2:
                if words[i - 1][j] != words[i][j]:
                    if not source:
                        source = words[i - 1][j]

                    g[words[i - 1][j]].append(words[i][j])

                    valid = True
                    break
                j += 1
            if not valid and l1 > l2:
                return ""

        res = []
        visited = set()
        path = set()

        hasCycle = False

        def toplogicSort(v):
            nonlocal hasCycle
            if v in visited:
                return
            if v in path:
                hasCycle = True
                return
            path.add(v)

            if v in g:
                for u in g[v]:
                    toplogicSort(u)
            path.remove(v)
            visited.add(v)
            res.append(v)

        toplogicSort(source)
        for v in g.keys():
            toplogicSort(v)

        if hasCycle:
            return ""

        for word in words:
            for letter in word:
                if letter not in visited:
                    visited.add(letter)
                    res.append(letter)

        res.reverse()
        return "".join(res)

        