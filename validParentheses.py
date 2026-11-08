class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if char == ')' and a != '(':
                    return False
                if char == '}' and a != '{':
                    return False
                if char == ']' and a != '[':
                    return False
        return False if stack else True