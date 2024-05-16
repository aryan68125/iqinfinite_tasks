# program to convert Set into Tuple and Tuple into Set 
'''
Input: {'a', 'b', 'c', 'd', 'e'}
Output: ('a', 'c', 'b', 'e', 'd')
Explanation: converting Set to tuple

Input: ('x', 'y', 'z')
Output: {'z', 'x', 'y'}
Explanation: Converting tuple to set
'''
# program to convert Set into Tuple and Tuple into Set : Solution
class Convert:
    def __init__(self, var_sets):
        self.__var_sets = var_sets
    def get_sets(self):
        return self.__var_sets
    def convert_sets(self):
        var_sets = self.__var_sets
        return tuple(var_sets)
    def convert_list(self):
        var_sets = self.__var_sets
        return list(var_sets)
    def convert_string(self):
        var_sets = self.__var_sets
        return str(var_sets)