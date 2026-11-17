class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack_index = -1

        for a in asteroids:
            while stack_index >= 0 and asteroids[stack_index] > 0 and a < 0:
                top = asteroids[stack_index]
                if top > abs(a):
                    a = 0
                    break
                elif top == abs(a):
                    stack_index -= 1
                    a = 0
                    break

                else:
                    stack_index -= 1
            if a:
                stack_index += 1
                asteroids[stack_index] = a
                

        return asteroids[  :stack_index  + 1]