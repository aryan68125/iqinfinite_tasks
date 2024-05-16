'''
this file returns the length of a string
'''
class Length:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def length_of_string(self):
        length_of_word = len(self.__word)
        return length_of_word