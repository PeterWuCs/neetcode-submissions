class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        wait = {}
        count = {}

        for i in range(len(tasks)):
            if count.get(tasks[i]):
                count[tasks[i]] += 1
            else:
                count[tasks[i]] = 1
        heap = []

        for key in count:
            heap.append(- count[key])

        heapq.heapify(heap)


        ans = 0
        while heap or wait:
            ans += 1

            if heap:
                cur = heapq.heappop(heap)
                if - cur > 1:
                    cur += 1
                    wait[ans + n] = cur
            
            if wait.get(ans):
                add = wait.pop(ans)
                heapq.heappush(heap, add)
        return ans


             
                

        