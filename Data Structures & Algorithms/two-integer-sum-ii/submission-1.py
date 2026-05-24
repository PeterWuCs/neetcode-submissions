class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            num = numbers[i] + numbers[j]

            if num == target:
                return [i+1 , j +1]

            if num > target:
                j -= 1
            else:
                i += 1
        
        return [i, j]