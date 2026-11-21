class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [False] * (n + 1)
        memo[0] = True

        for i in range(1, n +1):
            for word in wordDict:
                if i >= len(word):
                    j = i - len(word)
                    if s[ j : i ] == word and memo[j]:
                        memo[i] = True
        return memo[-1]