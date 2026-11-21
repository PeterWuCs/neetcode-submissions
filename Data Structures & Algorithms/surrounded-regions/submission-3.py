class Solution:
    def solve(self, board: List[List[str]]) -> None:
        reachable = set()

        n = len(board)
        m = len(board[0])   

        q = deque()

        for i in range(n):
            if board[i][0] == 'O':
                q.append((i, 0))

            if board[i][m - 1] == 'O':
                q.append((i, m - 1))

        for j in range(m):
            if board[0][j] == 'O':
                q.append((0, j))

            if board[n - 1][j] == 'O':
                q.append((n - 1, j))

        while q:
            i, j = q.popleft()
            print(i, j)

            if i < 0 or j < 0 or j >= m or i >= n or board[i][j] == 'X' or (i, j) in reachable:
                continue
            
            reachable.add((i, j))
            possible = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            for row, col in possible:
                if 0 <= row <= n - 1 and 0 <= col <= m - 1:
                    q.append((row, col))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in reachable:
                    board[i][j] = "X"

        