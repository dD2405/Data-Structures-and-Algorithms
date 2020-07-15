class Stack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def push(self,x):
        self.arr.append(x)

        if(self.min_stack == []):
            self.min_stack.append(x)
        else:
            if(x < self.min_stack[-1]):
                self.min_stack.append(x)
            

    def pop(self):
        if(self.arr == []):
            return None
        else:
            self.arr.pop()

    def top(self):
        if(self.arr == []):
            return -1
        else:
            return self.arr[-1]

    def getMin(self):
        if(self.min_stack == []):
            return -1
        else:
            return self.min_stack[-1]

    def print(self):
        print(self.arr)

s = Stack()

s.push(6)
s.push(7)
s.push(8)
s.print()
print(s.getMin())
s.pop()
print(s.top())
s.print()
