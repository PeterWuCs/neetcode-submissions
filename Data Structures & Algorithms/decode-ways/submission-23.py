class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        if n == 1:
            return 1

        chatList = [int(char) for char in s]
        
        first = 1
        second = 1

        if chatList[1] == 0 and chatList[0] > 2:
                return 0
        elif chatList[1] != 0 and chatList[0]*10 + chatList[1] < 27:
            second = 2

        for i in range(2, n):
            temp = second
            if not chatList[i - 1]:
                if not chatList[i]:
                    return 0

            elif not chatList[i]:
                if chatList[i - 1] > 2:
                    return 0
                second = first
            else:
                if not chatList[i - 1]*10 + chatList[i] >= 27:
                    second = first + second
            first = temp

        return second