class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        self.freq_dict = {}
        self.link_list_dict = {}

        self.key_dict = {}

        self.least_freq_count = 0


    def get(self, key: int) -> int:
        if key not in self.key_dict:
            return -1

        freq = self.freq_dict[key]

        remove_from = self.link_list_dict[freq]

        if freq + 1 not in self.link_list_dict:
            self.link_list_dict[freq + 1] = LinkList()

        add_to = self.link_list_dict[freq + 1]

        node = remove_from.pop(key)

        add_to.addRight(node)

        if remove_from.length() == 0:
            self.link_list_dict.pop(freq)

            if freq == self.least_freq_count:
                self.least_freq_count += 1
        
        self.freq_dict[key] += 1

        return self.key_dict[key]


    def put(self, key: int, value: int) -> None:
        
        if key in self.key_dict:

            freq = self.freq_dict[key]
            link_list = self.link_list_dict[freq]

            node = link_list.pop(key)

            if freq + 1 not in self.link_list_dict:
                self.link_list_dict[freq + 1] = LinkList()

            add_to = self.link_list_dict[freq + 1]

            add_to.addRight(node)

            self.key_dict[key] = value
            self.freq_dict[key] = freq + 1

            if link_list.length() == 0:
                self.link_list_dict.pop(freq)

                if freq == self.least_freq_count:
                    self.least_freq_count += 1

            return
        
        if len(self.key_dict) == self.cap:
            remove_from = self.link_list_dict[self.least_freq_count]
            node = remove_from.popLeft()

            self.key_dict.pop(node.key)
            self.freq_dict.pop(node.key)
            if remove_from.length() == 0:
                self.link_list_dict.pop(self.least_freq_count)


        node = Node(key=key)

        self.freq_dict[key] = 1
        self.key_dict[key] = value
        self.least_freq_count = 1

        if 1 not in self.link_list_dict:
            self.link_list_dict[1] = LinkList()

        add_to = self.link_list_dict[1]

        add_to.addRight(node)




class Node:
    def __init__(self, key=0, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LinkList:
    def __init__(self):
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

        self.key_dict = {}
    
    def popLeft(self):
        node = self.left.next

        self.left.next = self.left.next.next
        self.left.next.prev = self.left

        self.key_dict.pop(node.key)

        return node
        
    def addRight(self, node):
        temp = self.right.prev

        self.right.prev = node
        node.next = self.right
        temp.next = node
        node.prev = temp

        self.key_dict[node.key] = node
        
    def pop(self, key):
        node = self.key_dict[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        self.key_dict.pop(key)

        return node

    def length(self):

        return len(self.key_dict)








# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)