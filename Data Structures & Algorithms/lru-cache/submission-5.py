class Node:
    def __init__(self, key, val):
       self.key = key
       self.val = val
       self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)

        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next =next
        next.prev = prev

    def insert(self, node):

        last = self.right.prev

        last.next = self.right.prev = node

        node.next = self.right
        node.prev = last
        

    def get(self, key: int) -> int:
        if key in self.cache:

            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        new_Node = Node(key, value)

        if key in self.cache:
            self.remove(self.cache[key])

        self.insert(new_Node)
        self.cache[key] = new_Node

        if len(self.cache) > self.cap:
            to_remove = self.left.next
            self.remove(to_remove)
            del self.cache[to_remove.key]

        
