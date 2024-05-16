'''
This file caluclates chars in a string without spaces
'''
class LengthWithoutSpaces:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def length_without_spaces(self):
        w_string = self.__word
        res = sum(not chr.isspace() for chr in w_string)
        return res