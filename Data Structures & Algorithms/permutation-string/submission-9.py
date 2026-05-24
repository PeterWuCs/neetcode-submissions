class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        lengthT = len(s2)
        if length > lengthT:
            return False
        count = [0]* 26
        s2Count = [0]* 26
        
        for i in range(length):
            count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0

        for i in range(26):
            if count[i] == s2Count[i]:
                matches += 1

        if matches == 26:
            return True
        left, right  = 0, length - 1

        while right < lengthT - 1:
            right += 1
            s2Count[ord(s2[right]) - ord('a')] += 1

            if s2Count[ord(s2[right]) - ord('a')] == count[ord(s2[right]) - ord('a')]:
                matches += 1
            else:
                if s2Count[ord(s2[right]) - ord('a')] - 1== count[ord(s2[right]) - ord('a')]:
                    matches -= 1
            s2Count[ord(s2[left]) - ord('a')] -= 1

            if s2Count[ord(s2[left]) - ord('a')] == count[ord(s2[left]) - ord('a')]:
                matches += 1
            else:
                if s2Count[ord(s2[left]) - ord('a')] + 1 == count[ord(s2[left]) - ord('a')]:
                    matches -= 1
            left += 1
            if matches == 26:
                return True

        return False

        
