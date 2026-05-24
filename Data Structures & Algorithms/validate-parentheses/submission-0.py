class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {')': '(', ']': '[' , '}': '{'}

        for i in range(len(s)):
            if s[i] not in a.keys():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != a[s[i]]:
                    return False
        
        return len(stack) == 0