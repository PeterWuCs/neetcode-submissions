class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        curr = 0

        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                if tokens[i] == '+':
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    curr = a + b
                elif tokens[i] == '-':
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    curr = a - b
                elif tokens[i] == '*':
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    curr = a * b
                elif tokens[i] == '/':
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    if (a <= 0 and b <= 0) or (a >= 0 and b >= 0):
                        curr = a // b
                    else:
                        curr = - (-a // b)
            else:
                curr = int(tokens[i])
            
            stack.append(curr)

        return curr