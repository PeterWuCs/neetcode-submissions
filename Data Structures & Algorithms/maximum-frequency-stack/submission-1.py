class FreqStack:

    def __init__(self):
        self.stacks = []
        self.count_dict = defaultdict(int)

    def push(self, val: int) -> None:
        self.count_dict[val] += 1

        if len(self.stacks) < self.count_dict[val]:
            self.stacks.append([])
        
        self.stacks[self.count_dict[val] - 1].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
            
        self.count_dict[val] -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()