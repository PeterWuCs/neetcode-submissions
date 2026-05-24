class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = length
        for i in range(2, length + 1):
            odd = True if i % 2 == 1 else False
            for j in range(0, length - i + 1):
                substring = s[j : j + i]
                print(substring)
                if substring == substring[::-1]:
                    count += 1

        return count
