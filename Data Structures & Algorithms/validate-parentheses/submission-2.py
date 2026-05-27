class Solution:
    def isValid(self, s: str) -> bool:
        m={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]
        for i in s:
            if i in m:
                if not stack:
                    return False
                x=stack.pop()
                if x!=m[i]:
                    return False
            elif i in m.values():
                stack.append(i)
            else:
                return False
        if stack:
            return False
        return True
