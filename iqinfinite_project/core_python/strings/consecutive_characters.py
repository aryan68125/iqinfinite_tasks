# Consecutive characters frequency
'''
compute the frequency of consecutive characters till the character changes
'''
# Consecutive characters frequency : solution

from itertools import groupby
class ConsecutiveCharacters:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def consecutive_word(self):
        test_str = self.__word
        res = [len(list(j)) for _, j in groupby(test_str)]
        return res