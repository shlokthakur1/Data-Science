from referential_array import build_array

class arrayList:
    def __init__(self,size):
        self.array = build_array(size)
        self.maxSize = size
        self.currentLen = 0

    def __str__(self):
        string = ""
        for index in range(self.maxSize):
            string += str(self.array[index])
            string += ","
        return string
    def __len__(self):
        raise NotImplementedError

    def add(self,item):
        if (self.currentLen >= self.maxSize):
            raise IndexError("arrayList is full")
        self.array[self.currentLen] = item
        self.currentLen+=1

    def delete(self,position):
        if position >= self.currentLen:
            raise IndexError("index is empty")
        if self.array[position] is None:
            raise IndexError("index is empty")
        while position < self.currentLen and position < self.maxSize-1:
            self.array[position] = self.array[position+1]
            position += 1
        self.array[position] = None
        self.currentLen-=1

def testDelete():
    F = arrayList(5)
    try:
        F.delete(0)
    except IndexError:
        pass
    F.add(1)
    F.add(2)
    F.add(3)
    F.delete(2)
    assert str(F)=="1,2,None,None,None,"
    F.add(4)
    F.delete(1)
    assert str(F)=="1,4,None,None,None,"
    F.add(5)
    F.add(6)
    F.add(7)
    F.delete(2)
    print(F)



def testAdd():
    F = arrayList(5)
    # add to an empty list
    F.add(1)
    assert str(F)=="1,None,None,None,None,"
    # add without an item
    try:
        F.add()
    except TypeError:
        pass
    except:
        raise AssertionError("should have been a type error")
    #not empty addd
    F.add(2)
    # full list
    assert str(F)=="1,2,None,None,None,"
    F.add(3)
    F.add(4)
    F.add(5)
    try:
        F.add(6)
    except IndexError:
        pass
        #print(e)
        #assert str(e)=="IndexError: arrayList is full"
    #out of range




testAdd()
testDelete()