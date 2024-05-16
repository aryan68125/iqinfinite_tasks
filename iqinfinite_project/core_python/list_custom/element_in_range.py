# Test if List contains elements in Range
'''
Test if List contains elements in Range
'''
# Test if List contains elements in Range : Solution
class ListElementInRange:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def list_element_in_range(self,i,j):
        var_list = self.__var_list
        '''
        initialization of range : start = i, end = j
        ''' 
        res = all(ele >= i and ele < j for ele in var_list)
        return res
