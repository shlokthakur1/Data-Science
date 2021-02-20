class LetterTrieNode:
    def __init__(self):
        self.count = 1
        self.children = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
                         None,None,None,None,None,None,None,None]
        self.endOfString = False
        self.indice = -1

class LetterTrie:
    def __init__(self):
        self.root = LetterTrieNode()
        self.wordlist = []

    def insert(self,string,indice):
        current_node = self.root
        for i in range(len(string)):
            index = ord(str(string[i]))-97
            if current_node.children[index] == None:
                current_node.children[index] = LetterTrieNode()
            current_node = current_node.children[index]
        current_node.endOfString = True
        current_node.indice = indice


    def traverse(self, current_node, cur_string):
        if current_node.endOfString == True:
            self.wordlist.append(current_node.indice)
            #print(cur_string)
        for c in range(26):
            if current_node.children[c] != None:
                new_string = cur_string +chr(c+97)
                self.traverse(current_node.children[c],new_string)

    def search(self,substring):
        isPrefix = False
        current_node = self.root
        for i in range(len(substring)):
            index = ord(str(substring[i])) - 97
            if current_node.children[index] != None:
                isPrefix = True
            elif current_node.children[index] == None:
                isPrefix = False
                break
            current_node = current_node.children[index]
        if isPrefix== False:
            pass
        else:
            self.traverse(current_node,substring)

class NumberTrieNode:
    def __init__(self):
        self.count = 1
        self.children = [None,None,None,None,None,None,None,None,None,None]
        self.endOfString = False
        self.indice = -1

class NumberTrie:
    def __init__(self):
        self.root = NumberTrieNode()
        self.wordlist = []

    def insert(self,string,indice):
        current_node = self.root
        for i in range(len(string)):
            index = ord(str(string[i]))-48
            if current_node.children[index] == None:
                current_node.children[index] = NumberTrieNode()
            current_node = current_node.children[index]
        current_node.endOfString = True
        current_node.indice = indice


    def traverse(self, current_node, cur_string):
        if current_node.endOfString == True:
            self.wordlist.append(current_node.indice)
        for c in range(10):
            if current_node.children[c] != None:
                new_string = cur_string +chr(c+48)
                self.traverse(current_node.children[c],new_string)

    def search(self,substring):
        isPrefix = False
        current_node = self.root
        for i in range(len(substring)):
            index = ord(str(substring[i])) - 48
            if current_node.children[index] != None:
                isPrefix = True
            elif current_node.children[index] == None:
                isPrefix = False
                break
            current_node = current_node.children[index]
        if isPrefix== False:
            pass
        else:
            self.traverse(current_node,substring)

def query(filename,id_prefix,last_name_prefix):
    """
    Functionality of the function is that it searches the Trie and finds the records
    of those that match the inputted prefixes
    Time complexity: Best: O(N^2)
                    Worst: O(1)
    Space complexity: Best: O(N^2)
                    Worst: O(1)
    Error handle: if filename doesnt exist tell user
    Return: the index of id_prefix and last_name_prefix matches
    Parameter: filename,id_prefix,last_name_prefix
    Precondition: All 3 parameters should be strings

    """
    with open(filename) as file:
        fileList = file.read().splitlines()
    database = []
    for records in fileList:
        recordlist = []
        string = ""
        for character in records:
            if character != " ":
                string += character
            else:
                recordlist.append(string)
                string = ""
        database.append(recordlist)
    # print(database)
    id_database = []
    for records in database:
        id_database.append([records[0], records[1]])
    # print(id_database)
    last_name_database = []
    for records in database:
        last_name_database.append([records[0],records[3]])
    # print(last_name_database)

    last_name_trie = LetterTrie()
    for names in last_name_database:
        #print(names[1])
        last_name_trie.insert(names[1],names[0])
    last_name_trie.search(last_name_prefix)
    #print(last_name_trie.wordlist)
    #print(id_prefix)

    id_trie = NumberTrie()
    for ids in id_database:
        # print(names[1])
        id_trie.insert(ids[1],ids[0])
    id_trie.search(id_prefix)
    #print(id_trie.wordlist)

    id_prefix_list = id_trie.wordlist
    last_name_prefix_list = last_name_trie.wordlist
    return id_prefix_list,last_name_prefix_list

def findCommon(id_result,last_name_result):
    """
    Functionality of the function is to find common value between two lists and return
    the commons
        Time complexity: Best: O(N^2)
        Worst: O(1)
        Space complexity: Best:O(1)
        Worst:O(N^2)
        Error handle: None
        Return: List with the common indices of the two parameters
        Parameter: two lists that indicate the indices the prefixes are present
        Precondition: the parameters must be lists
    """
    finalResult = []
    for ids in id_result:
        for last_name in last_name_result:
            if ids == last_name:
                finalResult.append(ids)
    print(finalResult)

def reverseString(filename):
    """
    Functionality of the function is to find the index of substring whose
    reverses also exist within the string and print them
        Time complexity: Best: O(N^2+P)
        Worst: O(N^2+P+P*N)
        Space complexity: Best:O(N^2+P)
        Worst:O(N^2+P)
        Error handle: check if filename exists, if not tell the user
        Return: None
        Parameter: filename which is the name of the file we open
        Precondition: filename must be a string
    """
    def find_reverse_string(string):
        """
        Functionality of the function is to reverse a string
        Time complexity: Best: O(N^2)
        Worst:O(N^2)
        Space complexity: Best:O(N^2)
        Worst:O(N^2)
        Error handle: None
        Return: reversed string
        Parameter: string
        Precondition: string must be a string
        """
        return_string = ""
        for i in range(len(string) - 1, -1, -1):
            return_string += string[i]
        return return_string

    def RaddixSort(list):
        """
        Functionality of the function is to sort a list
        Time complexity: Best: O(N)
        Worst:O(N)
        Space complexity: Best:O(N)
        Worst:O(N)
        Error handle: None
        Return: a sorted list
        Parameter: list
        Precondition: list must be a list
        """
        def check_max_word_size(wordList):
            max_length = 0
            for word in wordList:
                if len(word) > max_length:
                    max_length = len(word)

            return max_length

        def set_same_size(wordList, max_size):
            new_list = []
            for words in wordList:
                spare_space = ['$' * (max_size - len(words))]
                new_list.append(words + ''.join(spare_space))
            return new_list

        max_size = check_max_word_size(list)
        same_size_list = (set_same_size(list, max_size))
        # print(same_size_list)

        buckets = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                   [],
                   []]
        returnList = same_size_list.copy().copy()
        # print(returnList)
        m = max_size
        for i in range(max_size):
            for words in returnList:
                s = ((words[m - 1 - i]))
                bucket_index = ord(s) - 96
                if bucket_index == -60:
                    bucket_index = 0
                buckets[bucket_index].append(words)
            # print(buckets)
            returnList = []
            for i in buckets:
                for j in i:
                    returnList.append(j)
            buckets = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                       [],
                       [],
                       []]
        # print(returnList)
        return returnList

    def build_suffixes(string):
        """
        Functionality of the function is to build all the suffixes of
        a given string
        Time complexity: Best: O(N^2)
        Worst:O(N^2)
        Space complexity: Best:O(N^2)
        Worst:O(N^2)
        Error handle: None
        Return: a list containing all the suffixes
        Parameter: string
        Precondition: string must be a string
        """
        suffix_array = []
        for i in range(len(string)):
            k = string[i:]
            q = string[:i]
            suffix_array.append(k + q)
        return suffix_array

    def bwt_matrixCreate(string):
        """
        Functionality of the function is to create a bwt_matrix for a given string
        Time complexity: Best: O(N^2)
        Worst:O(N^2)
        Space complexity: Best:O(N^2)
        Worst:O(N^2)
        Error handle: None
        Return: a list containing the sorted version of the suffix list created before
        Parameter: a string
        Precondition: string must be a string

        """
        suffix_array = build_suffixes(string)
        bwt_matrix = RaddixSort(suffix_array)
        return bwt_matrix

    def bwt_transform(string):
        """
        Functionality of the function is to get the bwt from a bwt_matrix
        Time complexity: Best: O(N^2)
        Worst:O(N^2)
        Space complexity: Best:O(N^2)
        Worst:O(N^2)
        Error handle: None
        Return: list of the bwt
        Parameter: string
        Precondition: string must be a string
        """
        bwt_matrix = bwt_matrixCreate(string)
        last_column = []
        for row in bwt_matrix:
            last_column.append(row[-1:])
        return last_column

    def bwt_statistic(bwt):
        """
        Functionality of the function is to generate the rank and occurence of a bwt
        Time complexity: Best:O(N)
        Worst:O(N)
        Space complexity: Best:O(N)
        Worst:O(N)
        Error handle:None
        Return: rank list and an occurence list
        Parameter: bwt
        Precondition: bwt should be a list
        """
        n = len(bwt)
        count = [0] * 26
        rank = [0] * 26
        occurrence = [[0] * (n) for i in range(26)]
        for i in range(n):
            if bwt[i] != "$":
                count[ord(bwt[i]) - 97] += 1
            for c in range(26):
                occurrence[c][i] = count[c]
        for i in range(n):
            for c in range(26):
                occurrence[c][0] = 0
        location = 1
        for c in range(26):
            rank[c] = location
            location += count[c]
        return rank, occurrence

    def bwt_substring_search(substring, rank, occurrence):
        """
Functionality of the function is to find the start and stop range of a substring in the bwt_matrix
        Time complexity: Best:O(N)
        Worst:O(N)
        Space complexity: Best:O(N)
        Worst:O(N)
        Error handle:none
        Return: start and stop
        Parameter:substring,ranklist and occurence list
        Precondition: substring must be a substring of the string, rank list should be of that string
        and occurrence list should be the same.
        """
        m = len(substring)
        start = 1
        end = len(string) - 1  # can do len(string)
        for i in range(m - 1, -1, -1):
            cur_letter_index = ord(substring[i]) - 97
            if start > end:
                break
            start = rank[cur_letter_index] + occurrence[cur_letter_index][start - 1]
            end = rank[cur_letter_index] + occurrence[cur_letter_index][end] - 1
        return start, end

    def find_substrings(string):
        """
        Functionality of the function is to find all substrings of a given string
        Time complexity: Best: O(N^2)
        Worst:O(N^2)
        Space complexity: Best:O(N^2)
        Worst:O(N^2)
        Error handle:None
        Return:substringList
        Parameter: a string
        Precondition:string should be a string
        """
        q = len(string)
        substringList1 = []
        for i in range(q - 1):
            substringList1.append(string[i:])
        # print(substringList1)
        substringList2 = []
        for word in substringList1:
            for i in range(1, q + 1):
                substringList2.append(word[:-i])
        # print(substringList2)
        for i in substringList2:
            if i != "" and len(i) > 1:
                substringList1.append(i)
        substringList = substringList1
        # print(substringList)
        return substringList

    def build_suffix_array(suffixes, bwt_matrix):
        """
        Functionality of the function is to build a suffix array
        Time complexity: Best: O(N^2)
        Worst:O(N^2)
        Space complexity: Best:O(N)
        Worst:O(N)
        Error handle:None
        Return: a suffix array
        Parameter:suffixes which is a list of all the suffixes of a string and
        bwt_matrix which is a bwt_matrix of a string
        Precondition: both parameters must be lists
        """
        suffix_array = [0] * len(suffixes)
        for i in range(len(bwt_matrix)):
            for j in range(len(suffixes)):
                if bwt_matrix[i] == suffixes[j]:
                    suffix_array[i] = j

        return suffix_array

    try:
        with open(filename) as file:
            string_word = file.read().splitlines()
        generic_string = string_word[0]  # "cabcdbadccc"#"xxabayyy"
        string = generic_string + "$"
        generic_reverse_string = find_reverse_string(generic_string)  # "cccdabdcbac"#"yyyabaxx"
        reverse_string = generic_reverse_string + "$"
        l = len(string)

        ###NORMAL BWT STUFF###
        bwt_matrix = bwt_matrixCreate(string)
        bwt = bwt_transform(string)
        bwt_statistics = bwt_statistic(bwt)
        rank = bwt_statistics[0]
        occurrence = bwt_statistics[1]
        suffixes = build_suffixes(string)

        ###REVERSE BWT STUFF###
        #reverse_bwt_matrix = bwt_matrixCreate(reverse_string)
        reverse_bwt = bwt_transform(reverse_string)
        reverse_statistics = bwt_statistic(reverse_bwt)
        #reverse_rank = reverse_statistics[0]
        #reverse_occurrence = reverse_statistics[1]
        reverse_suffixes = build_suffixes(reverse_string)

        #n = len(bwt)
        #reverse_substringList = find_substrings(generic_reverse_string)
        substringList = find_substrings(generic_string)

        class LookUpTrie:
            def __init__(self):
                self.root = LetterTrieNode()
                self.wordlist = []

            def insert(self, string):
                current_node = self.root
                for i in range(len(string)):
                    if string[i] == "$":
                        current_node.endOfString = True
                        break
                    index = ord(str(string[i])) - 97
                    if current_node.children[index] == None:
                        current_node.children[index] = LetterTrieNode()
                    current_node = current_node.children[index]
                current_node.endOfString = True

            def lookup(self, substring):
                isPrefix = False
                current_node = self.root
                for i in range(len(substring)):
                    index = ord(str(substring[i])) - 97
                    if current_node.children[index] != None:
                        isPrefix = True
                    elif current_node.children[index] == None:
                        isPrefix = False
                        break
                    current_node = current_node.children[index]
                return isPrefix

            def insert_find_indice(self, string, indice):
                current_node = self.root
                for i in range(len(string)):
                    if string[i] == "$":
                        current_node.endOfString = True
                        break
                    index = ord(str(string[i])) - 97
                    if current_node.children[index] == None:
                        current_node.children[index] = LetterTrieNode()
                    current_node = current_node.children[index]
                current_node.indice = indice
                current_node.endOfString = True

            def find_indice(self, substring):
                isPrefix = False
                current_node = self.root
                for i in range(len(substring)):
                    index = ord(str(substring[i])) - 97
                    if current_node.children[index] != None:
                        isPrefix = True
                    elif current_node.children[index] == None:
                        isPrefix = False
                        break
                    current_node = current_node.children[index]
                if isPrefix:
                    print(current_node.indice)

        suffix_array = build_suffix_array(suffixes, bwt_matrix)

        def findIndex(reverse_suffixes, suffix_array):
            """
            Functionality of the function is to find the index where the substring exists using the
            suffix array
            Time complexity: Best:O(N^2)
            Worst:O(N^2)
            Space complexity: Best:O(N)
            Worst:O(N)
            Error handle:None
            Return:None
            Parameter: reverse suffixes which contains suffixes of the reverse string
             and suffix array which contains indices where the substring start
            Precondition: both must be lists
            """
            T = LookUpTrie()
            for i in reverse_suffixes:
                T.insert(i)

            reverseOutputList = []
            for i in substringList:
                if T.lookup(i) == True:
                    reverseOutputList.append(i)

            reverseOutputList = list(set(reverseOutputList))
            indexList = []
            for i in reverseOutputList:
                OutputRange = bwt_substring_search(i, rank, occurrence)
                start = OutputRange[0]
                stop = OutputRange[1]
                index = (i, (start, stop))
                indexList.append(index)

            printList = []
            for i in indexList:
                InspectRange = i[1]
                start = InspectRange[0]
                stop = InspectRange[1]
                for j in range(start, stop + 1):
                    printList.append([i[0], suffix_array[j]])
            print(printList)

        findIndex(reverse_suffixes, suffix_array)
    except FileNotFoundError:
        print("This file does not exist")
        quit()


if __name__ == "__main__":
    result = (query("database.txt","2","Will"))
    id_result = result[0]
    last_name_result = result[1]
    findCommon(id_result,last_name_result)
    reverseString("test.txt")
