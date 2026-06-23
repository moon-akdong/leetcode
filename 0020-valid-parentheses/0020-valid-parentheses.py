class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            ")": "(",
            "]":"[",
            "}":"{",
        }
        stack = [] 

        for i in s:
            if i not in table:
                stack.append(i)
            
            elif not stack or table[i] != stack.pop():
                return False
        return len(stack) == 0