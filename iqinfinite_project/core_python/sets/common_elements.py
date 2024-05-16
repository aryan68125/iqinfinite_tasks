# Check if two lists have at-least one element common
'''
Input : a = [1, 2, 3, 4, 5]
        b = [5, 6, 7, 8, 9]
Output : True

Input : a=[1, 2, 3, 4, 5]
        b=[6, 7, 8, 9]
Output : False
'''
# Check if two lists have at-least one element common : Solution
class AtLeastOneCommonElements:
    def __init__(self,var_list_one, var_list_two):
        self.__var_list_one = var_list_one
        self.__var_list_two = var_list_two
    def get_list_one(self):
        return self.__var_list_one
    def get_list_two(self):
        return self.__var_list_two
    def at_least_common_elements(self):
        var_list_one = self.__var_list_one
        var_list_two = self.__var_list_two
        a_set = set(var_list_one)
        b_set = set(var_list_two)
        if (a_set & b_set):
            return True
        else:
            return False
