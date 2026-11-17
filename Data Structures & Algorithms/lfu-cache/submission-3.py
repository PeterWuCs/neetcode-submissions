class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0

        self.freq_dict = {}
        self.val_dict = {}

        self.start = Node()
        self.end = Node()
        
        self.start.next = self.end
        self.end.prev = self.start



    def get(self, key: int) -> int:
        if key not in self.val_dict:
            return -1
        
        node = self.val_dict[key]
        new_freq = node.freq + 1

        if new_freq in self.freq_dict:
            start = self.freq_dict[new_freq]
        else:
            start = self.freq_dict[node.freq]

        if self.freq_dict[new_freq - 1] == node:
            if node.next == self.end or node.next.freq != new_freq - 1:
                self.freq_dict.pop(new_freq - 1)
            else:
                self.freq_dict[new_freq - 1] = node.next

        if start is not node:

            node.prev.next = node.next
            node.next.prev = node.prev

            temp = start.prev
            
            start.prev = node
            temp.next = node
            node.prev = temp
            node.next = start
            
        
        self.freq_dict[new_freq] = node
        node.freq = new_freq

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.val_dict:

            node = self.val_dict[key]
            new_freq = node.freq + 1

            if new_freq in self.freq_dict:
                start = self.freq_dict[new_freq]
            else:
                start = self.freq_dict[node.freq]

            if self.freq_dict[new_freq - 1] == node:
                if node.next == self.end or node.next.freq != new_freq - 1:
                    self.freq_dict.pop(new_freq - 1)
                else:
                    self.freq_dict[new_freq - 1] = node.next

            if start is not node:

                node.prev.next = node.next
                node.next.prev = node.prev

                temp = start.prev

                start.prev = node
                temp.next = node
                node.prev = temp
                node.next = start
            
            node.val = value
            node.freq = new_freq

            self.freq_dict[new_freq] = node
            self.val_dict[key] = node
            return
        
        new_node = Node(val=value, key=key)

        if self.count == self.cap:
            least_freq_count = self.end.prev.freq

            if self.freq_dict[least_freq_count] == self.end.prev:
                self.freq_dict.pop(least_freq_count)

            self.val_dict.pop(self.end.prev.key)

            temp = self.end.prev.prev
            self.end.prev = temp
            temp.next = self.end

        if 1 in self.freq_dict:
            start = self.freq_dict[1]
        else:
            start = self.end
        
        temp = start.prev
        start.prev = new_node
        temp.next = new_node
        new_node.prev = temp
        new_node.next = start

        self.freq_dict[1] = new_node
        self.val_dict[key] = new_node

        self.count = len(self.val_dict)

        
        

 

            

        

        

class Node:
    def __init__(self, val=0, key=0, prev=None, next=None, freq=1):
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = freq
        self.key = key


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)