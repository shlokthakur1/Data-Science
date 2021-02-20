from referential_array import build_array

class arrayStack:
    def __init__(self,size):
        self.array = build_array(size)
        self.maxSize = size
        self.top = 0

    def __str__(self):
        string = "Stack:"
        for index in range(self.top):
            string += " "+str(self.array[index])
        return string + "<- top"

    def push(self,item):
        if self.top >= self.maxSize:
            raise StopIteration("the stack is full")
        self.array[self.top] = item
        self.top+=1

    def pop(self):
        if self.top==0:
            raise StopIteration("Stack is empty")
        self.top -= 1
        item = self.array[self.top]
        return item
"""
S = arrayStack(5)
#S.pop() #test passed triggered stop iteration
S.push(20)
print(S)
S.push(4)
print(S)
print(S.pop(),"and stack is now",str(S))
S.push(5)
S.push(6)
S.push(7)
S.push(8)
S.push(10000)
"""
