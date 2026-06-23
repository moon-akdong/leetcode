class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            ")": "(",
            "]":"[",
            "}":"{",
        }
        stack = [] 

        for i in s:
            if not stack or i not in table:
                stack.append(i)
            
            elif table[i] != stack.pop():
                return False
        return len(stack) == 0