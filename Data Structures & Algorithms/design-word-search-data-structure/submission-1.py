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
        return self.P_search(word, self.root)


        
    def P_search(self, word: str, node: Node):
        if not word:
            return node.isWord
        
        if word[0] == '.':
            for key in node.children:
                if self.P_search(word[1:], node.children[key]):
                    return True
            return False

        if word[0] in node.children:
            return self.P_search(word[1:], node.children[word[0]])
        return False
    



class Node:
    def __init__(self, isWord=False, children=None):
        self.isWord = isWord
        self.children = children
    