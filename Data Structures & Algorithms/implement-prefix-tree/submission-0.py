class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        root = self.root

        for a in word:
            if root.letter_dict.get(a):
                root = root.letter_dict[a]
            else:
                root.letter_dict[a] = Node()
                root = root.letter_dict[a]
        root.isWord = True


    def search(self, word: str) -> bool:
        root = self.root
        for a in word:
            if root.letter_dict.get(a):
                root = root.letter_dict[a]
            else:
                return False
        return root.isWord
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for a in prefix:
            if root.letter_dict.get(a):
                root = root.letter_dict[a]
            else:
                return False
        return True
    
class Node:
    
    def __init__(self, isWord=False, letter_dict={}):
        self.isWord = isWord
        self.letter_dict = {}
