class Decipher:
    def __init__(self):
        self.message = ""

    def messageFind(self,filename):
        """
        Functionality of the function
        The function of this method is to read the two lines and find the LCS of these two. Then once we get the table of
        the DP solution of the longest length LCS, we can use this function to map through it and find what strings were
        used to make the LCS. We do this from a bottom-up order so at the end we need to reverse the output, then add it
        to the instance variable self.message.

        Time Complexity:O(nm)
        Space Complexity:O(nm)
        Error handle: If encrypted file is empty, tell the user and exit the program
                        Also if the filename doesnt exist, tells user that it doesnt exist
        Return: None
        Parameter: filename - the name of the file we want to open to see the encrypted lines
        Pre-requisite: filename must be a string and there must be 2 lines in the file.
        """
        try:
            with open(filename) as file:
                encrypted_word = file.read().splitlines()
            if len(encrypted_word)==0:
                print("The encrypted file is empty")
                print("Program End")
                quit()
            #print(encrypted_word)
            string1 = encrypted_word[0]
            string2 = encrypted_word[1]
            n = len(string1)
            m = len(string2)
            array = self.LCS(string1, string2, n, m)
            k = len(string1)
            q = len(string2)
            string = []
            while k > 0 and q > 0:
                current_value = array[k][q]
                top_value = array[k - 1][q]
                left_value = array[k][q - 1]
                max_value = max(top_value, left_value)

                if current_value > max_value:
                    string.append(string1[k - 1])
                    k -= 1
                    q -= 1
                elif top_value > left_value:
                    k -= 1
                elif left_value > top_value:
                    q -= 1
                elif left_value == top_value:
                    k -= 1
            for i in range(len(string) - 1, -1, -1):
                self.message += str(string[i])
            #cannot return anything
            #return self.message
        except FileNotFoundError:
            print("Encrypted file not found")

    def LCS(self,string1, string2, n, m):
        """
        Functionality of the function
        The function of this method is to create a table which has the DP solution to the LCS problem of string1 and string2
        containing the max possible length of the LCS.

        Time Complexity:O(nm)
        Space Complexity:O(nm)
        Error handle:
        Return: array of the DP table, of the integer length of the LCS
        Parameter:  string1 - one string which is used in LCS
                    string2- another string which is used in LCS
                    n - the length of string1
                    m - the length of string2
        Pre-requisite:  string1, string2 must be strings
                        n, m must be integers
        """
        array = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    array[i][j] = 0
                elif string1[i - 1] == string2[j - 1]:
                    array[i][j] = array[i - 1][j - 1] + 1
                else:
                    array[i][j] = max(array[i - 1][j], array[i][j - 1])
        #for x in array:
            #print(x)
        return array

    def wordBreak(self,filename):
        """
        The function of this method is to go through the deciphered message and uncover the best word breaks to ensure that the
        maximum length character words are used.

        Time Complexity:O(km*nm)
        Space Complexity:O(km*nm)
        Error handle: If dictionary file has no words, returns the deciphered message as it as the True message
                        If the filename is incorrect tells the user it doesnt exist and returns the
                        deciphered message as is
        Return: None
        Parameter: filename - the name of the file we want to open to see the dictionary and based on thos split the lines
        Pre-requisite: filename must be a string and there must be 2 lines in the file.
        """
        try:
            with open(filename) as file:
                dictionary = file.read().splitlines()
            n = len(dictionary)
            k = len(self.message)
            encryptedword = self.message
            array = [[0] * (k + 1) for i in range(k + 1)]

            m = 0
            for i in dictionary:
                if len(i) > m:
                    m = len(i)

            for row in range(1, k + 1):
                string = ""
                for column in range(row, min(m + row, k + 1)):
                    string += encryptedword[column - 1]
                    index_we_place = -1
                    for x in range(n):
                        if string == dictionary[x]:
                            index_we_place = x
                    index_we_place += 1
                    if index_we_place > 0:
                        max_length1 = len(dictionary[index_we_place - 1])
                        top_value = array[row - 1][column]
                        max_value = max(len(dictionary[index_we_place - 1]), len(dictionary[array[row - 1][column] - 1]))
                        if top_value > 0:
                            max_length1 = max_value
                        if len(dictionary[index_we_place - 1]) == max_length1:
                            array[row][column] = index_we_place
                        else:
                            array[row][column] = array[row - 1][column]
                    elif index_we_place <= 0:
                        array[row][column] = array[row - 1][column]

            for row in range(1, k + 1):
                max_length2 = [0, 0]
                for column in range(row, min(m + row, k + 1)):
                    if array[row][column] != 0:
                        if len(dictionary[array[row][column] - 1]) > max_length2[0]:
                            max_length2[0] = len(dictionary[array[row][column] - 1])
                            max_length2[1] = array[row][column]
                    array[row][row] = max_length2[1]

            list = []
            for i in range(1, k + 1):
                list.append(array[i][i])
            #print(list)
            q = len(list)
            string = ""
            index = 0
            length = 1
            last_splitpoint = -1

            while index < q:
                # Base Case
                if index == q - 1:
                    for x in range(last_splitpoint + 1, index + 1):
                        string += encryptedword[x]
                    break

                if list[index] == list[index + 1]:
                    #print("CASE 1", index)
                    index += 1
                    length += 1
                elif list[index] != list[index] + 1:
                    # check if the current index is a zero, that means we have to backtrack until the last splitpoint
                    if list[index] == 0:
                        #print("CASE 2", index)

                        for x in range(last_splitpoint + 1, index + 1):
                            string += encryptedword[x]
                        string += " "
                        length = 1
                        last_splitpoint = index
                        index += 1

                    # check if what we've passed is a valid word
                    elif length == len(dictionary[list[index] - 1]):
                        #print("CASE 3", index)

                        for x in range(last_splitpoint + 1, index + 1):
                            string += encryptedword[x]
                        string += " "
                        length = 1
                        last_splitpoint = index
                        index += 1

                    # if not a valid word,back track all the way until the last splitpoint:
                    else:
                        #print("CASE 4", index)
                        for x in range(last_splitpoint + 1, index + 1):
                            string += encryptedword[x]
                        string += " "
                        length = 1
                        last_splitpoint = index
                        index += 1
            #print(string)
            self.message = string
        except FileNotFoundError:
            print("Dictionary file not found")

    def getMessage(self):
        """
        Time Complexity:O(1)
        Space Complexity:O(1)
        Error handle: None
        Return: self.message
        Parameter: filename - None
        Pre-requisite: None
        """
        return self.message

if __name__ == "__main__":
    D = Decipher()
    encryptedfilename = "encrypted1.txt"
    dictionaryfilename = "dictionary.txt"
    print("The name of the file, contains two encrypted texts :",encryptedfilename)
    print("The name of the dictionary file :",dictionaryfilename)
    D.messageFind(encryptedfilename)
    deciphered_message = D.getMessage()
    D.wordBreak(dictionaryfilename)
    true_message = D.getMessage()
    print("---------------------------------------------------------------------")
    print("Deciphered message is",deciphered_message)
    print("True message is",true_message)
    print("---------------------------------------------------------------------")
    print("Program End")
    quit()
