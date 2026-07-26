class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a set prevents duplicate vals 
        numSet = set(nums)
        longest = 0 

        for n in nums:
            # checks if a val is the start of the seq
            if (n-1 not in numSet):
                length = 0 
                # while sequential vals exist, it counts
                while (n + length) in numSet:
                    length += 1 
                longest = max(length, longest)
        return longest