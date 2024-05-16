# Flatten tuple of List to tuple
'''
Flattening a tuples involves converting a tuple of lists into single tuple
Input : test_tuple = ([5], [6], [3], [8]) 
Output : (5, 6, 3, 8) 
'''
# Flatten tuple of List to tuple : Solution
import sys
class FlattenTuple:
    def __init__(self, tuple):
        self.__tuple = tuple
    def get_tuple(self):
        return self.__tuple
    def flatten_tuple(self):
        tuple_var = self.__tuple
        temp_list = []
        for list in tuple_var:
            for element in list:
                temp_list.append(element)
        # res_tuple = tuple(temp_list)
        res_tuple = tuple(temp_list)
        return res_tuple