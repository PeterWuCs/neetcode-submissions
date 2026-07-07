class Solution:
    def countSubstrings(self, s: str) -> int:

        count = len(s)

        for i in range(count):
            left, right = i - 1, i + 1
            while left > -1 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            left, right = i - 1, i
            while left > -1 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count