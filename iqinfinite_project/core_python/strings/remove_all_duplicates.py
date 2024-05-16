# Remove all duplicates
'''
Input : geeksforgeeks 
Output : geksfor
'''
# Remove all duplicates : Solution
from collections import OrderedDict
class RemoveAllDuplicates:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def remove_all_duplicates(self):
        w_string = self.__word
        unique_string = "".join(OrderedDict.fromkeys(w_string))
        return unique_string
    
'''
:: THEORY ::
    OrderedDict.fromkeys(w_string): This part creates an OrderedDict from the characters of the string w_string.
        OrderedDict.fromkeys() method creates a new dictionary with keys from the iterable w_string and values set to None.
        Since OrderedDict maintains the order of insertion, the resulting OrderedDict will have keys in the same order as they appear in w_string.

    "".join(...): This part joins the keys of the OrderedDict into a single string.
        "".join() method joins the elements of an iterable (in this case, the keys of the OrderedDict) into a single string.
        Since the keys are characters from w_string, and they are ordered in the same order as they appear in w_string, the resulting string 
        will contain the characters from w_string in their original order.
'''
