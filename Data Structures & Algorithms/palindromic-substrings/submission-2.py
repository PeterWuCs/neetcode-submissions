class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        length = len(s)
        for i in range(length):
            right, left = i, i

            while left >= 0 and right < length:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break

        print(count)
        for i in range(length - 1):
            right, left = i + 1, i

            while left >= 0 and right < length:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break

        return count
