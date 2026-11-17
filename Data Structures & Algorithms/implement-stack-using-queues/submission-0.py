from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        if not self.q2:
            self.q1.append(x)
        else:
            self.q2.append(x)
        
    def pop(self) -> int:
        if self.empty():
            return -1

        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1

        while len(self.q1) != 0:
            ele = self.q1.popleft()
            if not self.q1:
                return ele
            self.q2.append(ele)

    def top(self) -> int:
        a = self.pop()
        if self.q1:
            self.q1.append(a)
        else:
            self.q2.append(a)
        return a

        

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()