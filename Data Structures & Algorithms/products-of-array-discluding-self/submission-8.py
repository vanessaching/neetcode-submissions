class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimized way 
        output = [1] * len(nums)

        # iterate from the beginning
        prefix = 1 
        for i in range(len(nums)):
            output[i] = prefix 
            prefix = prefix * nums[i]

        # iterate from the end 
        postfix = 1 
        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
        return output