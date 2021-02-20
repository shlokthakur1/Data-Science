class node:
    def __init__(self,value,link=None):
        self.value = value
        self.next = link

    def __str__(self):
        return "{"+str(self.value)+"}"

class linkedStack:
    def __init__(self):
        self.top = None

    def __str__(self):
        string = "Stack: Top"
        current = self.top
        while not (current is None):
            string += " -> " + str(current)
            current = current.next
        string += ""
        return string

    def isEmpty(self):
        return self.top is None

    def push(self,item):
        the_node = node(item)
        oldtop = self.top
        self.top = the_node
        the_node.next = oldtop

    def pop(self):
        if self.isEmpty():
            raise StopIteration("stack is empty")
        item = self.top.value
        self.top = self.top.next
        return item


S = linkedStack()
print(S)
S.pop()
S.push(1)
print(S)
S.push(2)
print(S)
S.push(3)
S.push(4)
S.pop()
S.push(5)
print(S)