class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        chars={')':'(', ']':'[','}':'{'}
        for i in s:
            if i in chars:
                if stack and stack[-1]==chars[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        