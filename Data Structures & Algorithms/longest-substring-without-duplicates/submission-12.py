class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        l = 0
        longest = 0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[l])
                l += 1
            a.add(s[i])
            longest = max(longest, i - l  + 1)
        return longest
