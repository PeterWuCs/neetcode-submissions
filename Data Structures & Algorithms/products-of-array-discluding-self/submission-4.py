class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [ 1 ]

        product = 1
        for i in range(0, len(nums) - 1):
            product = product * nums[i]
            output.append(product)
        
        print("output:", output)

        product = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            output[i] = output[i] * product
            product = product * nums[i]

        return output