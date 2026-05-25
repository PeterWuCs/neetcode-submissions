class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.cache = {}
        self.order_dict = {}   # key -> [prev, next]
        self.oldest = -1
        self.newest = -1

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            # Mark as used by moving to the end (most recent)
            self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        # Special case: capacity 1
        if self.cap == 1:
            self.cache = {key: value}
            self.oldest = key
            self.newest = key
            self.order_dict = {key: [-1, -1]}
            self.count = 1
            return

        # Case 1: Key already exists (update value and move to MRU)
        if key in self.cache:
            # If key is already the newest, just update value and return
            if key == self.newest:
                self.cache[key] = value
                return

            # Remove key from current position in linked list
            prev = self.order_dict[key][0]
            nxt = self.order_dict[key][1]

            if prev != -1:
                self.order_dict[prev][1] = nxt
            if nxt != -1:
                self.order_dict[nxt][0] = prev

            # Update oldest if we removed the head
            if key == self.oldest:
                self.oldest = nxt

            # If the list becomes empty after removal
            if prev == -1 and nxt == -1:
                self.oldest = -1
                self.newest = -1
            else:
                # Link the new key to the current newest
                self.order_dict[self.newest][1] = key

            # Add key as newest (tail)
            self.order_dict[key] = [self.newest, -1]
            self.newest = key
            self.cache[key] = value
            return

        # Case 2: Key is new, but cache has capacity left
        if self.count < self.cap:
            if self.count == 0:
                self.oldest = key
            else:
                self.order_dict[self.newest][1] = key
            self.order_dict[key] = [self.newest, -1]
            self.newest = key
            self.count += 1
            self.cache[key] = value
            return

        # Case 3: Key is new and cache is full -> evict LRU
        # Remove the oldest key
        evict_key = self.oldest
        nxt = self.order_dict[evict_key][1]

        # Update oldest pointer
        if nxt != -1:
            self.order_dict[nxt][0] = -1
        self.oldest = nxt

        # If the list becomes empty after eviction
        if nxt == -1:
            self.newest = -1

        # Clean up evicted key
        del self.cache[evict_key]
        del self.order_dict[evict_key]

        # Now add the new key as the newest
        if self.newest != -1:
            self.order_dict[self.newest][1] = key
        self.order_dict[key] = [self.newest, -1]
        self.newest = key

        # If this is the first element (cache was empty after eviction)
        if self.oldest == -1:
            self.oldest = key

        self.cache[key] = value