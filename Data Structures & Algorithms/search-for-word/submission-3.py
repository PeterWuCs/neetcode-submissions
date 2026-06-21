class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)

        m = len(board[0])

        def backTracking(i, j, hit, word):
            if not word:
                return True

            if i > 0 and ((i - 1, j) not in hit) and board[i - 1][j] == word[0]:
                hit.add((i - 1, j))
                right = backTracking(i - 1, j, hit, word[1:])
                if right:
                    return True
                hit.remove((i - 1, j))
            
            if j > 0 and ((i, j - 1) not in hit) and board[i][j - 1] == word[0]:
                hit.add((i, j - 1))
                right = backTracking(i, j - 1, hit, word[1:])
                if right:
                    return True
                hit.remove((i, j - 1))


            if i < n - 1 and ((i + 1, j) not in hit) and board[i + 1][j] == word[0]:
                hit.add((i + 1, j))
                right = backTracking(i + 1, j, hit, word[1:])
                if right:
                    return True
                hit.remove((i + 1, j))


            if j < m - 1 and ((i, j + 1) not in hit) and board[i][j + 1] == word[0]:
                hit.add((i, j + 1))
                right = backTracking(i , j + 1, hit, word[1:])
                if right:
                    return True
                hit.remove((i, j + 1))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    vit = set()
                    vit.add((i, j))
                    if backTracking(i, j, vit, word[1:]):
                        return True
        
        return False


