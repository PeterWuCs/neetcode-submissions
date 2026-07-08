class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        contains = {0}
        n = len(s)

        for i in range(n):
            for word in wordDict:
                startIndex = i - len(word) + 1
                if startIndex < 0:
                    continue
                if word == s[startIndex : i + 1] and startIndex in contains:
                    contains.add(i + 1)
        
        return n in contains

                            