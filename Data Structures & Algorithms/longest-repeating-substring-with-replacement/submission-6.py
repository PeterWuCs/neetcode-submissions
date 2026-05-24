class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        hash = [0] * 26
        
        l = 0
        for r in range(len(s)):
            hash[ord(s[r]) - ord('A')] += 1
            
            while (r - l + 1) - max(hash) > k:
                
                hash[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

            