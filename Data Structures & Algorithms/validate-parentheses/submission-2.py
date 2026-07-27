class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vals = {")":"(", "}":"{", "]":"["}

        for val in s: 
            if val in vals:
                if stack and stack[-1] == vals[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        return True if not stack else False