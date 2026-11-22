class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
        
        if endWord not in wordSet:
            return 0

        graph = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                possible = word[ : i] + "*" + word[i + 1: ]
                graph[possible].append(word)

        q = deque()
        q.append(beginWord)
        visited = set()

        count = 1

        while q:
            for i in range(len(q)):
                node = q.popleft()
                visited.add(node)

                if node == endWord:
                    return count
                
                for i in range(len(node)):
                    possible = node[ : i] + "*" + node[i + 1: ]
                    for nei in graph[possible]:
                        if nei not in visited:
                            q.append(nei)

            count += 1
        
        return 0














        