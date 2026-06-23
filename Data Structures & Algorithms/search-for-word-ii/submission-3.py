class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        T = Trie()
        n = len(board)
        m = len(board[0])

        for word in words:
            T.insert(word)

        index_set = set()
        res = set()
        temp = []

        def dfs(i, j, node):
            a = board[i][j]

            if a not in node.letter_dict:
                return

            node = node.letter_dict[a]

            index_set.add((i, j))
            temp.append(a)

            if node.isWord:
                res.add("".join(temp))

            possible_i_Move = []
            possible_j_Move = []

            if i > 0:
                possible_i_Move.append(-1)
            if i < n - 1:
                possible_i_Move.append(1)
            if j > 0:
                possible_j_Move.append(-1)
            if j < m - 1:
                possible_j_Move.append(1)

            for k in possible_i_Move:
                if (i+k, j) not in index_set:
                    dfs(i+k, j, node)

            for z in possible_j_Move:
                if (i, j+z) not in index_set:
                    dfs(i, j+z, node)

            temp.pop()
            index_set.remove((i, j))

            
        for i in range(n):
            for j in range(m):
                print("aaa")
                dfs(i, j, T.root)

        ans = [word for word in res]
        
        return ans

class Trie:

    def __init__(self):
        self.root = Node(letter_dict={})

    def insert(self, word: str) -> None:
        root = self.root
        for a in word:
            if root.letter_dict.get(a):
                root = root.letter_dict[a]
            else:
                root.letter_dict[a] = Node(letter_dict={})
                root = root.letter_dict[a]
        root.isWord = True

class Node:
    def __init__(self, isWord=False, letter_dict=None):
        self.isWord = isWord
        self.letter_dict = letter_dict

