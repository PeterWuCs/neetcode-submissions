class Solution:
    def solve(self, board: List[List[str]]) -> None:

        p = []

        n, m = len(board), len(board[0])

        for i in range(n):
            if board[i][0] == "O":
                p.append((i, 0))
            if board[i][m - 1] == "O":
                p.append((i, m - 1))

        for j in range(m):
            if board[0][j] == "O":
                p.append((0, j))
            if board[n - 1][j] == "O":
                p.append((n - 1, j))

        visited = set()


        while p:
            i, j = p.pop(0)
            visited.add((i, j))

            possible = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for item in possible:
                new_i = item[0] + i
                new_j = item[1] + j

                if -1 < new_i < n and -1 < new_j < m and board[new_i][new_j] == 'O' and (new_i, new_j) not in visited:
                    p.append((new_i, new_j))
            
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if (i, j) not in visited:
                    board[i][j] = "X"

