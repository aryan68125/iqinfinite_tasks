# Reverse Dictionary Keys Order
'''
The original dictionary : {‘is’: 2, ‘best’: 5, ‘gfg’: 4} 
The reversed order dictionary : OrderedDict([(‘gfg’, 4), (‘best’, 5), (‘is’, 2)])
'''
# Reverse Dictionary Keys Order : Solution

# Python3 code to demonstrate working of 
# Reverse Dictionary Keys Order
# Using OrderedDict() + reversed() + items()
from collections import OrderedDict
class ReverseDictionary:
    def __init__(self, var_dictionary):
        self.__var_dictionary = var_dictionary
    def get_dictionary(self):
        return self.__var_dictionary
    def reverse_dictionary(self):
        test_dict = self.__var_dictionary
        res = OrderedDict(reversed(list(test_dict.items())))
        return str(res)