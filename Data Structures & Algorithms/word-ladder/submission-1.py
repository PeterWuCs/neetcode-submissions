class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)

        wordList.append(beginWord)

        n = len(wordList)
        k = len(beginWord)

        for i in range(n):
            for z in range(k):
                possible = wordList[i][ :z] + '*' + wordList[i][ z+ 1:]
                g[possible].append(wordList[i])


        visited = set()
        p = [ beginWord ]
        q = []

        res = 1

        while p:
            new_word = p.pop(0)
            if new_word == endWord:
                return res
            
            visited.add(new_word)


            for z in range(k):
                possible = new_word[:z] + '*' + new_word[z+ 1:]
                for v in g[possible]:
                    if v not in visited:
                        q.append(v)

            if not p:
                q, p = p, q
                res += 1

        return 0

            


        