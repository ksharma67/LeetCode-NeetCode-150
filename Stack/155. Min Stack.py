class MinStack:

    def __init__(self):
        self.A = []
        self.M = []
        
    def push(self, x):
        self.A.append(x)
        M = self.M
        M.append( x if not M else min(x,M[-1]) )
        
    def pop(self):
        self.A.pop()
        self.M.pop()
        
    def top(self):
        return self.A[-1]
    
    def getMin(self):
        return self.M[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
