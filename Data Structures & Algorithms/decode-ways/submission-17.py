class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        
        if n == 1:
            return 1

        chatList = [int(char) for char in s]
        count = [-1] * n

        count[0] = 1
        if chatList[1] == 0:
            if chatList[0] > 2:
                return 0
            count[1] = 1
        else:
            if chatList[0]*10 + chatList[1] >= 27:
                count[1] = 1
            else:
                count[1] = 2


        for i in range(2, n):
            if not chatList[i - 1]:
                if not chatList[i]:
                    return 0
                count[i] = count[i - 1]
                continue

            if not chatList[i]:
                if chatList[i - 1]*10 + chatList[i] >= 27:
                    return 0
                if i - 2 >= 0:
                    count[i] = count[i - 2]
                else:
                    count[i] = count[i - 1]

            else:
                if chatList[i - 1]*10 + chatList[i] >= 27:
                    count[i] = count[i - 1]
                else:
                    count[i] = count[i - 1] + count[i - 2]



        print(count)
        return count[-1]