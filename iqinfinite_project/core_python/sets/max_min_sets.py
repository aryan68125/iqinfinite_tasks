# Maximum and Minimum in a Set
'''
Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
Output : max is 65

Input : set = ([4, 12, 10, 9, 4, 13])
Output : min is 4
'''
# Maximum and Minimum in a Set : Solution

class MaxElementsSets : 
    def __init__(self,var_sets):
        self.__var_sets = var_sets
    def get_sets(self):
        return self.__var_sets
    def max_element(self):
        var_sets = self.__var_sets
        return max(var_sets)
    def min_element(self):
        var_sets = self.__var_sets
        return min(var_sets)