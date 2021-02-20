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
class arrayQueue:
    def __init__(self,size):
        self.array = build_array(size)
        self.maxSize = size
        self.rear = 0
        self.front = 0

    def __str__(self):
        string = "Queue: front ->"
        for index in range(self.front,self.rear):
            string += " "+str(self.array[index])
        return string + "<- rear"

    def append(self,item):
        if self.rear >= self.maxSize:
            raise StopIteration("the queue is full")
        self.array[self.rear] = item
        self.rear += 1

    def serve(self):
        if self.rear == 0:
            raise StopIteration("queue is empty")
        item = self.array[self.front]
        position = self.front
        while position < self.rear and position < self.maxSize-1:
            self.array[position] = self.array[position+1]
            position += 1
        self.array[position] = None
        self.rear -= 1
        return item

Q = arrayQueue(5)
#Q.serve() #should yell
Q.append(1)
print(Q)
Q.append(2)
Q.append(3)
Q.append(4)
Q.append(5)
print(Q)
#Q.append(6) #should yell
print(Q.serve(),str(Q)) #should pass back '1'
