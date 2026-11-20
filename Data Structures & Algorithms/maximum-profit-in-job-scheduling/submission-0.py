class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        job = []
        n = len(startTime)

        for i in range(n):
            job.append((startTime[i], endTime[i], profit[i]))

        job.sort()
        next = [0] * n

        for j in range(n):
            f = job[j][1]

            low, high = j + 1, n - 1
            
            while low <= high:
                mid = (low + high) // 2

                if job[mid][0] < f:
                    low = mid + 1
                elif job[mid][0] > f:
                    next[j] = mid
                    high = mid - 1
                else:
                    next[j] = mid
                    break

            if next[j] == 0:
                next[j] = n
            
        memo = {}
        memo[n] = 0

        def helper(k):
            if k in memo:
                return memo[k]
            cur_pro = job[k][2]

            m = max(cur_pro + helper(next[k]), helper(k + 1))

            memo[k] = m

            return memo[k]
        return helper(0)

        