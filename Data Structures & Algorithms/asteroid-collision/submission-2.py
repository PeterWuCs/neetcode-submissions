class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            
            if stack[-1] * ast > 0:
                stack.append(ast)
                continue

            if stack[-1] < 0:
                stack.append(ast)
            else:
                while stack:
                    if stack[-1] * ast > 0:
                        stack.append(ast)
                        break

                    left = stack.pop()

                    if abs(left) > abs(ast):
                        stack.append(left)
                        break
                    elif abs(left) == abs(ast):
                        break
                    elif not stack:
                        stack.append(ast)
                        break

        return stack
