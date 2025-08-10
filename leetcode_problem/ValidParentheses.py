class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in pairs.values(): 
                stack.append(i)
            elif i in pairs:             
                if not stack or stack.pop() != pairs[i]:
                    return False
            else:
                return False               
        
        return not stack