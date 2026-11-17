class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for i in range(len(path)):
            char = path[i]

            if stack and stack[-1] == '.' and (char == '/' or (char == '.' and i == len(path) - 1)):
                
                if char == '.':
                    stack.append(char)

                if len(stack) > 2 and stack[-1] == '.' and stack[-2] == '.' and stack[-3] == '/':
                    count = 0

                    while count != 2 and stack:
                        remove = stack.pop()

                        if remove == '/':
                            count += 1
                
                elif len(stack) >= 2 and stack[-1] == '.' and stack[-2] == '/':
                    stack.pop()

                if char != '.' and (not stack or stack[-1] != '/'):
                    stack.append('/')
                continue


            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_':
                stack.append(char)
                continue
            
            elif char == '/' and (not stack or stack[-1] != '/'):
                stack.append('/')
                continue

            elif char == '.':
                stack.append('.')

        if stack[-1] == '.' and stack[-2] == '/':
            stack.pop()

        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()


        return "".join(stack)