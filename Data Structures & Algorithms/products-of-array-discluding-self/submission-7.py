class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the easy way 
        output = []
        product = 1
        zeroInList = 0
        for i in nums:
            if i != 0:
                product *= i
            if i == 0:
                zeroInList += 1 
        for val in nums:
            if zeroInList > 1:
                output.append(0)
            elif zeroInList == 1:
                if val == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(int(product/val)) 
        return output 