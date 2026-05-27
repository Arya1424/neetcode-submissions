class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            minval=val
        else:
            minval=min(self.stack[-1][1], val)
        self.stack.append([val,minval])
        

    def pop(self) -> None:
        val, minval=self.stack.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
