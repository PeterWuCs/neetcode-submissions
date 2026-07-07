class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ""

        n = len(s)

        for i in range(n):
            if (n - i) * 2 < longest:
                break

            left, right = i - 1, i + 1
            while left >= 0 and right <= n - 1 and s[right] == s[left]:
                left -= 1
                right += 1
            
            if right - left - 1 > longest:
                longest = right - left - 1
                res = s[left + 1 : right]

            left, right = i - 1, i
            while left >= 0 and right <= n - 1 and s[right] == s[left]:
                left -= 1
                right += 1

            if right - left - 1 > longest:
                longest = right - left - 1
                res = s[left + 1 : right]

        return res
        