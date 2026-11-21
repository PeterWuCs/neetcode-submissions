class LRUCache:

    def __init__(self, capacity: int):
        self.start = Node()
        self.end = Node()

        self.start.next = self.end
        self.end.prev = self.start

        self.key_dict = {}
        self.node_dict = {}

        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.key_dict:
            print("get key", key, -1)
            return -1
        
        key_node = self.node_dict[key]

        key_node.prev.next = key_node.next
        key_node.next.prev = key_node.prev

        temp = self.start.next

        self.start.next = key_node
        key_node.prev = self.start
        key_node.next = temp
        temp.prev = key_node
        return self.key_dict[key]
        

    def put(self, key: int, value: int) -> None:

        if key not in self.key_dict:
            node = Node(key=key)
            self.node_dict[key] = node

        else:
            node = self.node_dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev

        self.key_dict[key] = value

        temp = self.start.next
        
        self.start.next = node
        temp.prev = node

        node.next = temp
        node.prev = self.start


        if len(self.key_dict) > self.cap:
            delete_node = self.end.prev

            delete_node.prev.next = self.end
            delete_node.next.prev = delete_node.prev

            del self.key_dict[delete_node.key]
            del self.node_dict[delete_node.key]


class Node:

    def __init__(self, prev=None, next=None, key=-1):
        self.prev = prev
        self.next = next
        self.key = key
        
