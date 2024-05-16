# Remove duplicate lists in tuples(Preserving Order)
# Using OrderedDict() + tuple()
from collections import OrderedDict
class RemoveDuplicateTuples : 
    def __init__(self, var_tuple):
        self.__var_tuple = var_tuple
    def get_tuple(self):
        return self.__var_tuple
    def remove_duplicates(self):
        var_tuple = self.__var_tuple
        res = list(OrderedDict((tuple(x),x) for x in var_tuple).values())
        return res