from linkedStack import node

class linkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        string = "List: ("+str(len(self))+") "
        current = self.head
        while not (current is None):
            string += " -> " + str(current)
            current = current.next
        string += ""
        return string

    def getNode(self,index):
        current = self.head
        if index >= len(self) or index < 0:
            raise StopIteration("Node doesn't exist at this index")
        currentPos = 0
        while not current is None and currentPos<index:
            current = current.next
            currentPos += 1
        return current

    def insert(self,item,index):
        if index==0:
            self.head = node(item,self.head)
        else:
            someNode = self.getNode(index-1)
            someNode.next = node(item, someNode.next)
        self.count+=1

    def delete(self,index):
        if index==0:
            self.head = self.head.next
        else:
            before = self.getNode(index - 1)
            itemToRemove = before.next
            before.next = itemToRemove.next
        self.count-=1




aList = linkedList()
#aList.delete(1)
#aList.delete(0)
print(aList)
aList.insert("yeet",0)
print(aList)
aList.insert("boi",0)
print(aList)
aList.insert("awww snap",2)
print(aList)
aList.insert("awww snap2",len(aList))
print(aList)
aList.insert("awww snap3",len(aList))
print(aList)
aList.delete(0)
aList.insert("awww snap4",len(aList))
print(aList)
aList.insert("middle man",3)
print(aList)
aList.delete(1)
print(aList)
aList.delete(len(aList)-1)
print(aList)