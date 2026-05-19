class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(':0,'{':1,'[':2}
        closing = {')':0,'}':1,']':2}

        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack:
                    return False
                match = stack.pop()
                if opening[match] != closing.get(char):
                    return False
        return True if not stack else False
