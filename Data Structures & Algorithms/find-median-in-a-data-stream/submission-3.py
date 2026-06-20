class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_count = 0
        self.max_count = 0

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append(num)
            self.min_count += 1
            return
        if not self.max_heap:
            self.max_count += 1
            if self.min_heap[0] < num:
                smaller = self.min_heap.pop()
                self.max_heap.append(- smaller)
                self.min_heap.append(num)
            else:
                self.max_heap.append(- num)

            return
        
        if num <= - self.max_heap[0]:
            if self.min_count > self.max_count:
                heapq.heappush(self.max_heap, - num)
                self.max_count += 1
            else:
                med = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, - med)
                heapq.heappush(self.max_heap, - num)
                self.min_count += 1

        elif num >= self.min_heap[0]:
            if self.min_count == self.max_count:
                heapq.heappush(self.min_heap, num)
                self.min_count += 1
            else:
                med = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, - med)
                heapq.heappush(self.min_heap, num)
                self.max_count += 1

        else:
            if self.min_count == self.max_count:
                heapq.heappush(self.min_heap, num)
                self.min_count += 1
            else:
                heapq.heappush(self.max_heap, - num)
                self.max_count += 1


        

    def findMedian(self) -> float:
        print("min", self.min_heap)
        print("max", self.max_heap)
        if (self.min_count + self.max_count) %2 == 1:
            return self.min_heap[0]

        return (self.min_heap[0] - self.max_heap[0]) / 2
        