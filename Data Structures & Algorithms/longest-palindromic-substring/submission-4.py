class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = -1
        start = -1

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if longest < r - l + 1:
                        longest = r - l + 1
                        start = l
                    l -= 1
                    r += 1
                else:
                    break

            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if longest < r - l + 1:
                        longest = r - l + 1
                        start = l
                    l -= 1
                    r += 1
                else:
                    break

        return s[start : start + longest]