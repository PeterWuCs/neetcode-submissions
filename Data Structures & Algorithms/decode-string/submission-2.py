class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
                continue

            concat = []

            while True:
                element = stack.pop()

                if element != '[':
                    concat.append(element) 
                else:
                    break

            num_list = []

            while stack and  "0" <= stack[-1] <= '9':
                num_list.append(stack.pop())
            num_list.reverse()
            num = int("".join(num_list))

            concat.reverse()
            new_string = "".join(concat * num)

            stack.append(new_string)

        
        return "".join(stack)
