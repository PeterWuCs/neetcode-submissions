class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0 
        right = 0

        ans = []
        q = deque()

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            if not q or nums[right] <= nums[q[-1]]:
                q.append(right)


            if right - left + 1 < k:
                right += 1
                continue

            if left > q[0]:
                q.popleft()

            ans.append(nums[q[0]]) 

            left += 1
            right += 1


        return ans

