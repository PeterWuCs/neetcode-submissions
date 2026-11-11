class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            
            if nums[i] < 1:
                continue
            
            if nums[i] > n:
                continue

            if nums[i] is True:
                continue

            cur = nums[i]



            while cur >= 1 and cur <= n:
                if i == 2:
                    print(nums)
                temp = nums[cur - 1]
                nums[cur - 1] = True
                if i == 2:
                    print(temp)


                cur = temp

                if cur is True:
                    break

        print("final", nums)
        for i in range(n):
            if nums[i] is not True:
                return i + 1

        return n + 1