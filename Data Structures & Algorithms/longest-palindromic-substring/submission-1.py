class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        length = 0
        for i in range(len(s)):
            right, left = i, i
            temp1 = ""
            temp2 = ""

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                if right == left:
                    temp1 = s[left]
                else:
                    temp1 = s[left] + temp1 + s[left]
                    print(temp1)
                right += 1
                left -= 1

            right, left = i + 1, i
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                temp2 = s[left] + temp2 + s[left]
                right += 1
                left -= 1
            
            

            if len(temp1) > len(temp2):
                if len(temp1) > length:
                    longest = temp1
                    length = len(temp1)
            else:
                if len(temp2) > length:
                    longest = temp2
                    length = len(temp2)
        return longest
                
            


        