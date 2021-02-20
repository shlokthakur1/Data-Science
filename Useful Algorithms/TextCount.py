def Task1Processing(filename):
    """
    :param filename: this is the name of the file we want to read
    :return: returns a list containing only the words (after processing)
    This function opens the file, processes them then returns a list
    Time Complexity (Worst Case): O(N*M) where N is the number of words in the file and M is the Maximum amount
    of characters in a word
    """
    list = []
    list2 = []
    with open(filename) as file:
        lines = file.read().splitlines()
        for i in lines:
            list.append(i)
    for i in list:
        list2.append(i.split())
    list3 = []
    for words in list2:
        for characters in words:
            if characters != ".":
                if characters == "am":
                    pass
                elif characters == "is":
                    pass
                elif characters == "are":
                    pass
                elif characters == "was":
                    pass
                elif characters == "were":
                    pass
                elif characters == "has":
                    pass
                elif characters == "have":
                    pass
                elif characters == "had":
                    pass
                elif characters == "been":
                    pass
                elif characters == "will":
                    pass
                elif characters == "shall":
                    pass
                elif characters == "may":
                    pass
                elif characters == "can":
                    pass
                elif characters == "would":
                    pass
                elif characters == "should":
                    pass
                elif characters == "might":
                    pass
                elif characters == "could":
                    pass
                elif characters == "a":
                    pass
                elif characters == "an":
                    pass
                elif characters == "the":
                    pass
                else:
                    list3.append(characters)
    list4 = []
    for words in list3:
        words = words.strip(",")
        words = words.strip(".")
        words = words.strip('""')
        words = words.strip("?")
        words = words.strip("!")
        words = words.strip(":")
        words = words.strip(";")
        list4.append(words)

    finalList = []
    for items in list4:
        if items != "":
            finalList.append(items)

    return finalList


def check_max_word_size(aList):
    """
    :param aList: list of strings or integers
    :return: max_length: integer of the longest length item in the list
    checks through the list and finds the longest length string or integer in the list
    Time Complexity (Worst Case): O(N*M) where N is the number of words in the file and M is the Maximum amount
    of characters in a word
    """
    max_length = 0
    for word in aList:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


def set_same_size(aList, max_size):
    """
    :param aList: list of strings or integers
    :param max_size:integer of the longest length item in the list
    :return: new_list: which is a list that has combined the dots and words to match every item in the list to have
    the same length as the max size item

    Adds dots to the end of words that arent equal to the size of the length max_size which is inputted.

    Time Complexity (Worst Case): O(N) where N is the number of words in the list
    """
    new_list = []
    for words in aList:
        spare_space = ['.' * (max_size - len(words))]
        new_list.append(words + ''.join(spare_space))
    return new_list


def RaddixSort(aList):
    """
    :param aList: list of strings or integers
    :return: finalReturnList: a final sorted list
    This function sorts a aList in ascending order

    Time Complexity (Worst Case): O(N) where N is the number of words in the list
    """
    max_size = check_max_word_size(aList)
    same_size_list = (set_same_size(aList, max_size))

    buckets = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
               [], [],
               []]
    returnList = same_size_list
    m = max_size
    for i in range(max_size):
        for words in returnList:
            s = ((words[m - 1 - i]))
            bucket_index = ord(s) - 96
            if bucket_index == -50:
                bucket_index = 0
            buckets[bucket_index].append(words)
        returnList = []
        for i in buckets:
            for j in i:
                returnList.append(j)
        buckets = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                   [], [],
                   [],
                   []]
    finalReturnList = []
    for letters in returnList:
        letters = letters.strip(".")
        finalReturnList.append(letters)
    return finalReturnList

def frequencyList(aList):
    """
    :param aList: SORTED list of strings or integers
    :return: count_list: a list with every object and their respective count

    This function joins the [word, frequency] of the items in aList
    Time Complexity (Worst Case): O(N) where N is the number of words in the list
    """
    pos = 0
    n = len(aList)
    count_list = []
    while pos <= n:
        count = 1
        try:
            while aList[pos] == aList[pos + 1]:
                count += 1
                pos += 1
            count_list.append([aList[pos], count])
            pos += 1
        except IndexError:
            count_list.append([aList[pos], count])
            break
    return count_list

class MaxHeap:
    def __init__(self, aList):
        self.heap = [0]
        for i in aList:
            self.heap.append(i)
            self.rise(len(self.heap) - 1)

    def pop(self):
        """
        :return: returns the root of the MaxHeap which is the maximum value
        """
        if len(self.heap)>2:
            self.swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.sink(1)
        else:
            max = self.heap.pop()
        return max

    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def rise(self, index):
        """
        :param index: index of the position we want to rise up the heap
        :return: None

        Checks to see if the parents are greater than the current index, depending on the outcome it swaps or not

        Time Complexity (Worst Case): log(N) where N is the number of parents in the heap
        """
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index][1] > self.heap[parent][1]:
            self.swap(index,parent)
            self.rise(parent)

    def sink(self, index):
        """
        :param index: index of the position we want to sink down the heap
        :return: None

        Checks to see if the childs are smaller than the current index, depending on the outcome it swaps or not

        Time Complexity (Worst Case): log(N) where N is the number of children in the heap
        """
        left_child = index * 2
        right_child = index * 2 + 1
        largest_node = index
        n = len(self.heap)

        if left_child < n and self.heap[largest_node][1] < self.heap[left_child][1]:
            largest_node = left_child
        elif left_child<n and self.heap[largest_node][1] == self.heap[left_child][1]:
            if self.heap[largest_node][0] > self.heap[left_child][0]:
                largest_node = left_child

        if right_child<n and self.heap[largest_node][1] < self.heap[right_child][1]:
            largest_node = right_child
        elif right_child<n and self.heap[largest_node][1] == self.heap[right_child][1]:
            if self.heap[largest_node][0] > self.heap[right_child][0]:
                largest_node = right_child
        if largest_node != index:
            self.swap(index,largest_node)
            self.sink(largest_node)

play = True
while play != False:
    try:
        filename = input("Enter the filename:")
        finalList = Task1Processing(filename)
        print("Words are preprocessed...")
        if len(finalList) == 0:
            print("Unable to continue:")
            print('1. Writing.txt is empty or')
            print('2. There is no word remaining after preprocessing.')
            quit()
        Continue = input("Do I need to display the remaining words:")
        if Continue == 'Y':
            for i in finalList:
                print(i)
        else:
            print("Okay I won't then")
        setofFinalList = set(finalList)
        noDuplicatesList = []
        for i in setofFinalList:
            noDuplicatesList.append(i)
        sortedList = RaddixSort(finalList)
        print('The remaining words are sorted in alphabetical order')
        Continue1 = input("Do you want to see:")
        if Continue1 == 'Y':
            for i in sortedList:
                print(i)
        else:
            print("Okay I won't then")
        print("The Total number of words in the writing is:",len(finalList))
        print("The frequencies of each word:")
        printFreqList = [len(sortedList)]
        freqList = frequencyList(sortedList)
        printFreqList += freqList
        for i in range(len(freqList)):
            print(str(freqList[i][0]) + " : " + str(freqList[i][1]))

        k = int(input("What would you like k to be:"))
        if k > len(freqList):
            k = len(freqList)

        M = MaxHeap(freqList)
        kList = []
        for i in range(k):
            kList.append(M.pop())

        for i in range(len(kList)):
            print(str(kList[i][0]) + " : " + str(kList[i][1]))
        quit()

    except FileNotFoundError:
        print("Please enter a file that exists")
    except ValueError:
        print("Please enter an integer")



