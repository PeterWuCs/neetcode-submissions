class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        wait = [0] * (n + 1)
        comp = [0] * (n + 1)
        count = {}

        for i in range(len(tasks)):
            if count.get(tasks[i]):
                count[tasks[i]] += 1
            else:
                count[tasks[i]] = 1
        heap = []

        for key in count:
            heap.append((- count[key], key))

        heapq.heapify(heap)


        ans = 0
        while heap or wait != comp:

            print(heap)
            print(wait)
            ans += 1

            if wait[0] != 0:
                heapq.heappush(heap, wait[0])


            for i in range(n ):
                wait[i] = wait[i + 1]
            wait[n ] = 0

            if heap:
                cur = heapq.heappop(heap)
                if - cur[0] > 1:
                    cur = (cur[0] + 1, cur[1])
                    wait[n ] = cur
        return ans


             
                

        