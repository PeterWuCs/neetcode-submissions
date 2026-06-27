class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)

        wordList.append(beginWord)

        n = len(wordList)
        k = len(beginWord)

        for i in range(n):
            for j in range(i + 1, n):
                count = 0
                for z in range(k):
                    if wordList[i][z] != wordList[j][z]:
                        count += 1
                if count == 1:
                    g[wordList[i]].append(wordList[j])
                    g[wordList[j]].append(wordList[i])
        visited = set()
        p = [ beginWord ]
        q = []

        res = 1

        while p:
            new_word = p.pop(0)
            if new_word == endWord:
                return res
            
            visited.add(new_word)

            for v in g[new_word]:
                if v not in visited:
                    q.append(v)

            if not p:
                q, p = p, q
                res += 1

        return 0

            


        