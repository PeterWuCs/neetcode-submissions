class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set()

        for num in nums:
            a.add(num)

        b = set()
        for x in a:
            if x + 1 not in a or x - 1 in a:
                continue
            else:
                b.add(x)
                
        if len(b) == 0 and len(nums) != 0:
            return 1
        count = 0

        for x in b:
            inner_count = 1
            i = x + 1
            while i in a:
                i += 1
                inner_count += 1
            if inner_count > count:
                count = inner_count
        
        return count
            
