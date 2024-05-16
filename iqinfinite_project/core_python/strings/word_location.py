# Word location in String
'''
This will search the word in a string and return it's location in the strings
'''
# Word location in String : solution
import re

class WordLocation:
    def __init__(self,word,search):
        self.__word = word
        self.__search_word = search
    
    #getter and setter for word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    #getter and setter for word that is to be search
    #search word
    def get_search_word(self):
        return self.__search_word
    def set_search_word(self,word):
        self.__search_word = word

    def word_location(self):
        test_str = self.__word
        wrd = self.__search_word
        test_str = test_str.split()
        res = -1
        for idx in test_str:
            if len(re.findall(wrd, idx)) > 0:
                res = test_str.index(idx) + 1
        return res

