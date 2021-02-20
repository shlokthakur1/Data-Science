class linkedListIterator:
    def __init__(self,the_list):
        assert type(the_list)==type(linkedList())
        self.whereAmI = the_list.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.whereAmI is None:
            raise StopIteration
        returnedValue = self.whereAmI.value
        self.whereAmI = self.whereAmI.next
        return returnedValue