class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]* 26
        for s in s1:
            count[ord(s) - ord("a")] += 1

    
        left, right = 0, 0

        while right < len(s2):
            if count == [0] * 26:
                return True

            s = s2[right]
            index = ord(s) - ord("a")
            if count[index] == 0:
                count[ord(s2[left]) - ord("a")] += 1
                left += 1
            else:
                count[index] -= 1
                right += 1
        if count == [0] * 26:
                return True
        return False
