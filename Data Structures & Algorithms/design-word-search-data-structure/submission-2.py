class WordDictionary:

    def __init__(self):
        self.root = Node(children = {})
        
    def addWord(self, word: str) -> None:
        cur = self.root

        for a in word:
            if not cur.children.get(a):
                cur.children[a] = Node(children={})
            cur = cur.children[a]
        cur.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):

            for j in range(i, len(word)):
                if word[j] == '.':
                    for key in node.children:
                        if dfs(j + 1, node.children[key]):
                            return True
                    return False

                else:
                    if word[j] in node.children:
                        node = node.children[word[j]]
                    else:
                        return False
            return node.isWord
        return dfs(0, self.root)



class Node:
    def __init__(self, isWord=False, children=None):
        self.isWord = isWord
        self.children = children
    