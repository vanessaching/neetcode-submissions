class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() 

        for i, val in enumerate(nums):
            if i > 0 and nums[i - 1] == val:
                continue
            l = i + 1 
            r = len(nums) - 1 
            while l < r:
                sum = val + nums[l] + nums[r]
                if sum > 0:
                    r -= 1 
                elif sum < 0: 
                    l += 1 
                else: 
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result 
            