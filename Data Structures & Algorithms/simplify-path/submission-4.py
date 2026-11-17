class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        possible_dict = path.split('/')

        for folder in possible_dict:
            if not folder or folder == '.':
                continue
            if folder == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(folder)

        return '/' + "/".join(stack)