# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]
        self.size=0


    def push(self, x: int) -> None:
        if self.size==0:
            self.minstack.append(x)
        else:
            if x<=self.minstack[-1]:
                self.minstack.append(x)
        self.stack.append(x)
        self.size+=1

    def pop(self) -> None:
        t=self.stack.pop()
        self.size-=1
        if t==self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
