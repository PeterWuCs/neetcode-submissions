class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        res = []

        l = 0
        r = k
        n = len(arr)

        while r < n:
            if abs(arr[r] - x) < abs(arr[l] - x) or arr[r] == arr[l]:
                r += 1
                l += 1
            else:
                break


        return arr[l : r]

